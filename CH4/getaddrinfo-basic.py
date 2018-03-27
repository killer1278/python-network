#! /usr/bin/env python3
# Basic getaddrinfo() basic example - Chapter 4 - getaddrinfo-basic.py
# Usage: 。/getaddrinfo-basic.py www.baidu.com
import sys,socket

result = socket.getaddrinfo(sys.argv[1],None)
print(result[0][4])
