#! /usr/bin/env python3
# Basic inetd server - Chapter 3 - inetdserver.py

import sys
print("Welcome.")
print("Please enter a string:")
# 默认情况下，sys.stdout是被缓冲的
# 调用flush()函数，可以确保输出被立即传输。
sys.stdout.flush()
line = sys.stdin.readline().strip()
print("You entered %d characters."%len(line))
