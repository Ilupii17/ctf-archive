import zipfile
import glob
import os

EXTRACT_DIR = 'extracted'

os.makedirs(EXTRACT_DIR, exist_ok=True)

for zip_path in glob.glob("secret*.zip"):
    print(f"[+] Processing: {zip_path}")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(EXTRACT_DIR)
            print(f"    Extracted to: {EXTRACT_DIR}")

            # Baca semua file dalam ZIP
            for info in zf.infolist():
                extracted_file = os.path.join(EXTRACT_DIR, info.filename)

                # Pastikan file bukan direktori
                if not info.is_dir():
                    try:
                        with open(extracted_file, 'r', encoding='utf-8', errors='replace') as f:
                            print(f"\n--- {info.filename} ---")
                            print(f.read())
                    except Exception as e:
                        print(f"    [!] Gagal baca {info.filename}: {e}")
    except zipfile.BadZipFile:
        print(f"    [!] Bukan ZIP valid: {zip_path}")
