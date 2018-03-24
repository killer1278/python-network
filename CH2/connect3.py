#! /usr/bin/env python3
# Information Example - Chapter 2 - connect3.py
# 从socket获取信息。

import socket

print("Creating socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("done.\n")

print("Looking up port number...")
port = socket.getservbyname('http','tcp')
print('done.\n')

print("Connecting to remote host...")
s.connect(("www.baidu.com", port))
print("done.\n")

print("Connected from: ", s.getsockname())
print("Connected to: ", s.getpeername())
