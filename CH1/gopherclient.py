#! /usr/bin/env python3
# Simple Gopher Client - Chapter 1 - gopherclient.py

# 这是在现实世界可能找到的，可以运行的网络协议实现的最小程序。
# gopher协议是一种在web出现之前非常流行的协议。
# 脚本功能，知道主机名和文件名，从gopher服务器上请求对应文档。
# ./gopherclient.py quux.org / 

import socket, sys

port = 70       # Gopher uses port 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET, ip4;SOCK_STREAM,使用tcp协议通信
s.connect((host,port))
requestFile = filename + "\r\n"
s.sendall(bytes(requestFile,'utf-8'))

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(str(buf))
