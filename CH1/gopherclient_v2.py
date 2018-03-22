#! /usr/bin/env python3
# Simple Gopher Client - Chapter 1 - gopherclient_v2.py

# python库支持文件和文件类对象。socket对象则不提供类似的接口。
# 可以利用makefile()函数把socket对象生成一个文件类对象
# 这个脚本运行不会报错，但是也不返回结果，不知什么原因。

import socket, sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
fd = s.makefile('rw') # 对生成的套接字文件类对象有读写的权利
requestFile = filename + "\r\n"
fd.write(requestFile)

for line in fd.readlines():
    sys.stdout.write(line)
