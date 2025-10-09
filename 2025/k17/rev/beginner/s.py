#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
import sys
from typing import Dict, List, Tuple

# Each entry in the wasm data segment looks like:
# [4-byte LE index][32-hex ASCII][\x00][5-letter word ASCII][\x00]
# Example from your dump:
# \x11\x00\x00\x00 70e7726a9b8d5e65a6dbb19cf784ad5a \x00 zonal \x00

HEX_KEY_RE = re.compile(rb'[0-9a-f]{32}\x00')
WORD_RE    = re.compile(rb'[a-z]{5}\x00')

def parse_entries_from_wasm(data: bytes) -> List[Tuple[int, str, str, int]]:
    """
    Parse (index, key, word, offset) tuples from the wasm binary by pattern scanning.
    Returns a list sorted by index (not by offset).
    """
    entries: List[Tuple[int, str, str, int]] = []
    n = len(data)

    # We look for a hex key + null, followed by a 5-letter word + null,
    # and 4 bytes before the key that decode to a small positive integer index.
    pos = 0
    while True:
        m_key = HEX_KEY_RE.search(data, pos)
        if not m_key:
            break

        key_start = m_key.start()
        key_end = m_key.end()
        key_bytes = data[m_key.start():m_key.end()-1]  # strip trailing \x00
        # Sanity: charclass ensures key_bytes are ASCII hex.
        key = key_bytes.decode('ascii')

        # Try to parse the word immediately after the key+null
        word_match = WORD_RE.match(data, key_end)
        if word_match:
            word_bytes = data[word_match.start():word_match.end()-1]  # strip trailing \x00
            word = word_bytes.decode('ascii')

            # Try to read a 4-byte LE index right before the key
            idx_pos = key_start - 4
            if idx_pos >= 0:
                idx = int.from_bytes(data[idx_pos:key_start], byteorder='little', signed=False)

                # Heuristics: plausible indices are small positive ints (1..10000)
                if 0 <= idx < 100000:
                    entries.append((idx, key, word, idx_pos))

        # Move forward even if this attempt didn't yield a valid entry
        pos = m_key.start() + 1

    # Remove duplicates by preferring earliest offset, then sort by index
    # (Some binaries might embed multiple similar blocks; we keep first occurrence.)
    best_by_index: Dict[int, Tuple[int, str, str, int]] = {}
    for idx, key, word, off in entries:
        if idx not in best_by_index or off < best_by_index[idx][3]:
            best_by_index[idx] = (idx, key, word, off)

    result = list(best_by_index.values())
    result.sort(key=lambda t: t[0])
    return result


def build_index_maps(entries: List[Tuple[int, str, str, int]]):
    """
    Build lookup maps:
      - index_to_word: index -> word
      - index_to_key:  index -> key
    """
    index_to_word: Dict[int, str] = {}
    index_to_key: Dict[int, str] = {}
    for idx, key, word, _ in entries:
        index_to_word[idx] = word
        index_to_key[idx] = key
    return index_to_word, index_to_key


def get_word_for_day(day_number: int, index_to_word: Dict[int, str]) -> str:
    """
    Day numbers are 1-based in the game’s UI.
    From your wasm dump, the stored index appears 1-based as well (e.g., 17 -> 'zonal').
    So we look up directly by day_number.
    """
    if day_number not in index_to_word:
        raise KeyError(f"Day {day_number} not found in parsed table")
    return index_to_word[day_number]


def main():
    ap = argparse.ArgumentParser(description="Offline solver for Legally Distinct Daily Game")
    ap.add_argument("wasm", help="Path to words.wasm")
    ap.add_argument("days", nargs="*", type=int, default=[72, 73, 74],
                    help="Day numbers to query (default: 72 73 74)")
    ap.add_argument("--dump", action="store_true",
                    help="Dump all parsed entries (index, key, word)")
    args = ap.parse_args()

    if not os.path.exists(args.wasm):
        print(f"[-] File not found: {args.wasm}", file=sys.stderr)
        sys.exit(1)

    data = open(args.wasm, "rb").read()
    entries = parse_entries_from_wasm(data)

    if not entries:
        print("[-] No entries parsed. The binary format may differ or the pattern is off.", file=sys.stderr)
        sys.exit(2)

    index_to_word, index_to_key = build_index_maps(entries)

    if args.dump:
        for idx, key, word, _ in entries:
            print(f"{idx:4d}  {key}  {word}")
        print(f"[+] Parsed {len(entries)} entries.", file=sys.stderr)

    # Compute words
    words = []
    for d in args.days:
        w = get_word_for_day(d, index_to_word).lower()
        words.append((d, w))

    # If exactly 3 days (like the challenge), print in flag format, else list
    if len(words) == 3:
        print(f"K17{{{words[0][1]}, {words[1][1]}, {words[2][1]}}}")
    else:
        for d, w in words:
            print(f"{d}: {w}")


if __name__ == "__main__":
    main()
