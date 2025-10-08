import glob

real_png_header = b'\x89PNG\r\n\x1a\n'

for filename in glob.glob("photo*.png"):
    try:
        with open(filename, "rb") as f:
            data = f.read()

        if data[:8] == b"COMPFEST":
            print(f"[+] Fixing header: {filename}")
            fixed_data = real_png_header + data[8:]

            with open(filename, "wb") as f:
                f.write(fixed_data)
        else:
            print(f"[-] Skipping (already valid): {filename}")
    except Exception as e:
        print(f"[!] Error on {filename}: {e}")
