def solve():
    secret = [
        # v3
        0xE1, 0xA7, 0x1E, 0xF8, 0x75, 0x23, 0x7B, 0x61, 
        # v4
        0xB9, 0x9D, 0xFC, 0x5A, 0x5B, 0xDF, 0x69, 0xD2, 
        0xFE, 0x1B, 0xED, 0xF4, 0xED, 0x67, 0xF4
    ]

    # Siapkan array untuk menampung byte-byte flag
    flag_bytes = [0] * 27
    
    # Variabel untuk meniru state dari program C
    v10 = 0  # Bit index for input
    v11 = 0  # Byte index for input

    # Loop luar: 23 byte data rahasia (i dari 0 sampai 22)
    for i in range(23):
        # Loop dalam: 8 bit per byte rahasia
        for j in range(8):
            if v10 == 0:
                v10 = 1

            secret_byte = secret[i]
            secret_bit_mask = 1 << (7 - j)
            is_secret_bit_set = (secret_byte & secret_bit_mask) > 0

            flag_bit_mask = 1 << (7 - v10)
            if is_secret_bit_set:
                flag_bytes[v11] |= flag_bit_mask
            
            v10 += 1
            if v10 == 8:
                v10 = 0
                v11 += 1
            
            if v11 == 27:
                break
        if v11 == 27:
            break

    flag = "".join(chr(b) for b in flag_bytes)
    return flag

flag = solve()
print(f"Flag yang ditemukan: {flag}")
