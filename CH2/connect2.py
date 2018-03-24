#! /usr/bin/env python3
# Revised Connection Example - Chapter 2 - connect2.py
# 对上一个程序的修改，使用端口名而不是端口号。

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
