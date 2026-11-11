"""LLM-as-judge client with a disk cache.

Any OpenAI-compatible chat endpoint works (OpenAI, OpenRouter, a local server).
Every (model, prompt) pair is cached to a JSONL file, so re-running a report,
re-bucketing, or bootstrapping never re-pays a judge call. Delete the cache
file to re-judge.

Judge choice is a reported parameter of the protocol, not an implementation
detail: a judge from the same model family as the generator under test is a
known bias source (self-enhancement, Zheng et al. 2023). Report the judge model.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from typing import Optional, Protocol


class Judge(Protocol):
    model: str

    def ask(self, prompt: str) -> str: ...


def parse_json(text: str) -> dict:
    """Parse the judge's JSON, tolerating ``` fences and trailing prose."""
    t = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", t, flags=re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                pass
    return {}


def parse_score(text: str, key: str = "score", default: float = 0.0) -> float:
    data = parse_json(text)
    try:
        return max(0.0, min(1.0, float(data.get(key, default))))
    except (TypeError, ValueError):
        m = re.search(rf'"{key}"\s*:\s*([\d.]+)', text)
        return max(0.0, min(1.0, float(m.group(1)))) if m else default


class DiskCache:
    def __init__(self, path: Optional[str | Path]):
        self.path = Path(path) if path else None
        self._mem: dict[str, str] = {}
        if self.path and self.path.exists():
            with open(self.path, encoding="utf-8") as f:
                for line in f:
                    try:
                        row = json.loads(line)
                        self._mem[row["k"]] = row["v"]
                    except (json.JSONDecodeError, KeyError):
                        continue

    @staticmethod
    def key(model: str, prompt: str) -> str:
        return hashlib.sha256(f"{model}\x00{prompt}".encode("utf-8")).hexdigest()

    def get(self, k: str) -> Optional[str]:
        return self._mem.get(k)

    def put(self, k: str, v: str) -> None:
        self._mem[k] = v
        if self.path:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "a", encoding="utf-8") as f:
                f.write(json.dumps({"k": k, "v": v}, ensure_ascii=False) + "\n")


class OpenAICompatibleJudge:
    """Chat-completions judge. Env defaults: JUDGE_MODEL, JUDGE_API_KEY
    (falls back to OPENROUTER_API_KEY / OPENAI_API_KEY), JUDGE_BASE_URL."""

    def __init__(
        self,
        model: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        cache_path: Optional[str | Path] = None,
        temperature: float = 0.0,
        max_tokens: Optional[int] = None,
        system: Optional[str] = None,
    ):
        self.model = model or os.getenv("JUDGE_MODEL", "openai/gpt-4o-mini")
        # Non-OpenAI judges (Claude, Gemini) tend to write a claim-by-claim analysis BEFORE the
        # JSON; at 512 tokens the JSON is cut off and parse_score falls back to 0.0 (found 19 Oct
        # 2026: 57/111 faithfulness = 0.0 with claude-sonnet-4.6). A system instruction keeps the
        # output to the JSON object; a larger budget is the safety net. Both are part of the cache key.
        self.max_tokens = max_tokens or int(os.getenv("JUDGE_MAX_TOKENS", "512"))
        self.system = system if system is not None else os.getenv("JUDGE_SYSTEM", "")
        self.api_key = api_key or os.getenv("JUDGE_API_KEY") or os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("JUDGE_BASE_URL", "https://openrouter.ai/api/v1")
        self.temperature = temperature
        self.cache = DiskCache(cache_path)
        self.calls = 0
        self._client = None
        if not self.api_key:
            raise RuntimeError("No judge API key: set JUDGE_API_KEY (or OPENROUTER_API_KEY / OPENAI_API_KEY).")

    def _get_client(self):
        if self._client is None:
            from openai import OpenAI  # imported lazily: optional dependency

            self._client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        return self._client

    def ask(self, prompt: str) -> str:
        k = DiskCache.key(self.model, (self.system + "\n\n" if self.system else "") + prompt)
        hit = self.cache.get(k)
        if hit is not None:
            return hit
        messages = ([{"role": "system", "content": self.system}] if self.system else []) + [{"role": "user", "content": prompt}]
        resp = self._get_client().chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        out = (resp.choices[0].message.content or "").strip()
        self.calls += 1
        self.cache.put(k, out)
        return out


class MockJudge:
    """Deterministic judge for tests and the offline example. It does not
    understand anything: it answers from simple lexical overlap, so numbers it
    produces are meaningless beyond exercising the pipeline."""

    model = "mock"

    def __init__(self, threshold: float = 0.3):
        self.threshold = threshold
        self.calls = 0

    @staticmethod
    def _overlap(a: str, b: str) -> float:
        wa = set(re.findall(r"\w{4,}", a.lower()))
        wb = set(re.findall(r"\w{4,}", b.lower()))
        return len(wa & wb) / len(wa) if wa else 0.0

    def ask(self, prompt: str) -> str:
        self.calls += 1
        head, _, tail = prompt.partition("\n\n---\n\n")
        score = round(self._overlap(head, tail), 3)
        if '"relevant"' in prompt:
            return json.dumps({"relevant": score >= self.threshold})
        if '"supported"' in prompt:
            return json.dumps({"supported": score >= self.threshold, "reason": "mock"})
        return json.dumps({"score": score, "total_claims": 1, "supported_claims": int(score >= self.threshold)})
