from pwn import *

# stage 1 process
argv = list('1' * 100)
argv[0] = "./input"
argv[ord('A')] = "\x00"
argv[ord('B')] = "\x20\x0a\x0d"

# stage 2 stdio
with open("stdin.txt", "wb") as file:
    file.write("\x00\x0a\x00\xff")
    file.close()
with open("stderr.txt", "wb") as file:
    file.write("\x00\x0a\x02\xff")
    file.close()

# stage 3 env
env = {"\xde\xad\xbe\xef": "\xca\xfe\xba\xbe"}

# stage 4 file
with open("\x0a", "wb") as file:
    file.write("\x00\x00\x00\x00")
    file.close()

# stage 5 network
argv[ord('C')] = "9999"

p = process(argv=argv, env=env, stdin=open("stdin.txt","rb"), stderr=open("stderr.txt","rb"))
r = remote("127.0.0.1", 9999)
r.send("\xde\xad\xbe\xef")
r.close()

print p.recv()
print p.recv()
