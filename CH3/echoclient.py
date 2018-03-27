#! /usr/bin/env python3
# Echo client with deadlocak - Chapter 3 - echoclient.py
# 没有出现书中说的死锁问题，不知道为什么，一切都很正常。

import socket,sys
port = 51423
host = 'localhost'

data = b"x"*10475760 # 10MB of data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

byteswritten = 0
while byteswritten < len(data):
    startpos = byteswritten
    endpos = min(byteswritten + 1024, len(data))
    byteswritten += s.send(data[startpos:endpos])
    sys.stdout.write("Wrote %d bytes\r"%byteswritten)
    sys.stdout.flush()

s.shutdown(1)

print("All data sent.")
while 1:
    buf = s.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(str(buf))
