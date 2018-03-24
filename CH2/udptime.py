#! /usr/bin/env python3
# UDP Connectionless Example - Chapter 2 - udptime.py

import socket, sys, struct, time

host = 'time.nist.gov'
port = 37

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Send data to the socket. 
# The socket should not be connected to a remote socket, since the destination socket is specified by address. 
s.sendto(b'',(host,port))

print("Looking for replies; press Ctrl-C or Ctrl-Break to stop.")
# Receive data from the socket. 
# The return value is a pair (bytes, address).
buf = s.recvfrom(2048)[0]
if len(buf) != 4:
    print("Wrong-sized reply %d: %s"%(len(buf),buf))
    sys.exit(1)

secs = struct.unpack("!I",buf)[0]
secs -= 2208988800
print(time.ctime(int(secs)))
