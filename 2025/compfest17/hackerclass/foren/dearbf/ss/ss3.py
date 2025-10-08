import glob

# Header ZIP yang valid: 50 4B 03 04
valid_zip_header = b'\x50\x4B\x03\x04'

for filename in glob.glob("secret*.zip"):
    with open(filename, "rb") as f:
        data = f.read()

    if not data.startswith(valid_zip_header):
        print(f"[+] Fixing header: {filename}")
        fixed = valid_zip_header + data[4:]
        with open(filename, "wb") as f:
            f.write(fixed)
    else:
        print(f"[-] Already valid: {filename}")
