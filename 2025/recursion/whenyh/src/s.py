for c in range(ord('a'), ord('z') + 1):
    v = ((c - 0x57) % 26) + ord('a')
    if chr(v) == 'p':
        print(chr(c), "→", chr(v))
