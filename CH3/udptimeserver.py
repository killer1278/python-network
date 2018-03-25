#! /usr/bin/env python3
# UDP Wrong Time Server - Chapter 3 - udptimeserver.py
# 程序发送回昨天的日期。返回结果是一个bytes的struct。

import socket, traceback, time, struct

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((host,port))

while 1:
    try:
        message, address = s.recvfrom(8192)
        secs = int(time.time())    # Seconds since 1/1/1970
        secs -= 24 * 60 * 60       # Make it yesterday
        secs += 2208988800         # Convert to secs since 1/1/1900
        reply = struct.pack('!I',secs)
        s.sendto(reply, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
