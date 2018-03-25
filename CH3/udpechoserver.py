#! /usr/bin/env python3
# UDP Echo Server - Chapter 3 - udpechoserver.py
# 测试： ipython创建一个udp套接字，给这个服务器发送数据。

import socket, traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((host,port))
print("UDP Server is running...")

while 1:
    try:
        message, address = s.recvfrom(8192)
        print("Got data from", address)
        # Echo it back
        s.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        rasie
    except:
        traceback.print_exc()
