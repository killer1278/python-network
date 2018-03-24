#! /usr/bin/env python3
# Error Handling Example with Shutdown - Chapter 2 - shutdown.py

"""
失败， 没有找到原因
[root@django python-network]# ./shutdown.py zabbix.fan 80 /
Sleeping...
Continue.                               
"""

import socket, sys, time

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

print("Sleeping...")
time.sleep(180)
print("Continue.")
# 连接建立后，服务器过了一段时间没有收到请求，会自动断掉这个连接。
# 如果python客户端继续s.sendall(msg),不会产生异常。但s.recv不会有任何内容。
try:
    msg = "GET %s HTTP/1.1\r\n\r\n"%filename
    msg_bytes = msg.encode('utf-8')
    s.sendall(msg_bytes)
except socket.error as e:
    print("Error sending data: %s"%e)
    sys.exit(1)

# 对于一个来自对sendall()成功调用后返回的数据，并不可靠。
# 事实上这个请求可能永远没有被服务器接收到。
# 为了解决这个问题，一旦结束写操作，你应该立刻调用shutdown()函数。
# 这样就会强制清除缓存里面的内容。同时如果有任何问题就会产生一个异常。
try:
    s.shutdown(1)
except socket.error as e:
    print("Error sending data (detected by shutdown): %s"%e)
    sys.exit(1)
except :
    print("there is error after s.shutdown.")
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
                              
