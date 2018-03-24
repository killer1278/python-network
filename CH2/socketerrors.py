#! /usr/bin/env python3
# Error Handling Example - Chapter 2 - socketerrors.py
# Usage: ./socketerrors.py www.baidu.com http /

"""
python的socket模块定义了4种可能的异常：
    socket.error, 与一般I/O和通信问题有关
    socket.gaierror，与查询地址信息有关
    socket.herror，与其他地址错误有关
    socket.timeout, 处理超时有关
"""

import socket, sys

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Strange error creating socket: %s"%e)
    sys.exit(1)

# Try parsing it as a numeric port number.
try:
    port = int(textport)
except ValueError:
    # That didn't work, so it's probably a protocol name.
    # Look it up instead.
    try:
        port = socket.getservbyname(textport,'tcp')
    except socket.error as e:
        print("Couldn't find your port: %s"%e)
        sys.exit(1)

try:
    s.connect((host,port))
except socket.gaierror as e:
    print("Address-related error connecting to server: %s"%s)
    sys.exit(1)
except socket.error as e:
    print("Connection error: %s"%e)
    sys.exit(1)


try:
    msg = "GET %s HTTP/1.1\r\n\r\n"%filename
    msg_bytes = msg.encode('utf-8')
    s.sendall(msg_bytes)
except socket.error as e:
    print("Error sending data: %s"%e)
    sys.exit(1)

while 1:
    try:
        buf = s.recv(2048)
    except socket.error as e:
        print("Error receiving data: %s"%e)
        sys.exit(1)
    # 
    if not len(buf):
        break
    print(buf)
    
