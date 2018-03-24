#! /usr/bin/env python3
# UDP Example - Chapter 2 - udp.py
# Usage: ./udp.py localhost 51423
# 第三章有UPD应答服务器。

import socket, sys

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(textport)
except ValueError:
    # That didn't work. Look it up instead.
    port = socket.getservbyname(textport, 'udp')


s.connect((host,port))
print("Enter data to transmit: ")
data = sys.stdin.readline().strip()
s.sendall(data)
print("Looking for replies; press Ctrl-C or Ctrl-Break to stop.")
while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    print(buf)
