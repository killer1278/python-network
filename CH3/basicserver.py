#! /usr/bin/env python3
# Base Server - Chapter 3 - basicserver.py
# 测试：telnet localhost 51423

import socket

host = ''    # Bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# setsockopt(level, opt, value); level通常是SOL_SOCKET.
s.bind((host,port))
print("Waiting for connections...")
s.listen(1)

# 通常情况下，无限循环是不好的，因为会耗尽系统的CPU资源。
# 这里不同，调用accept()的时候，只在有一个客户端连接后才返回。
# 如果没有客户端连接，程序会停止。
while 1:
    clientsock, clientaddr = s.accept()
    print("Got connection from ", clientsock.getpeername())
    clientsock.close()
