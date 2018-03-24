#! /usr/bin/env python3
# Basic Connection Example - Chapter 2 - connect.py
# 创建socket.
# 这个例子连接上www.baidu.com上的web服务器，接着打印状态信息，最后终止。

import socket

print("Creating socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("done.\n")

print("Connecting to remote host...")
s.connect(("www.baidu.com",80))
print("done.\n")
