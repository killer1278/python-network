#! /usr/bin/env python3
# Basic DNS library example - Chapter 4 DNS-basic.py
# Usage: ./DNS-basic.py baidu.com

import sys,DNS

query = sys.argv[1]
DNS.DiscoverNameServers()

reqobj = DNS.Request()

answerobj = reqobj.req(name = query, qtype = DNS.Type.ANY)
if not len(answerobj.answers):
    print("Not found.")
for item in answerobj.answers:
    print("%-5s %s"%(item['typename'], item['data']))
