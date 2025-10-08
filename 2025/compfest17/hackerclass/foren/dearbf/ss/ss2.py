import glob

# Header JPG yang benar: FF D8 FF E0 00 10 4A 46 49 46 00
valid_jpg_header = b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00'

for filename in glob.glob("photo*.jpg"):
    with open(filename, "rb") as f:
        data = f.read()

    if not data.startswith(b'\xFF\xD8'):
        print(f"[+] Fixing header: {filename}")
        new_data = valid_jpg_header + data[10:]
        with open(filename, "wb") as f:
            f.write(new_data)
    else:
        print(f"[-] Already valid: {filename}")
