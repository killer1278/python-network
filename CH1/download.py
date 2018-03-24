#! /usr/bin/env python3
# Chapter 1 - Download Example - download.py
# Usage: ./download.py http://www.baidu.com/

import sys
from urllib.request import *

f = urlopen(sys.argv[1])
while 1:
    buf = f.read(2048)
    if not len(buf):
        break
    print(buf)
