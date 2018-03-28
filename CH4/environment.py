#! /usr/bin/env python3
# Basic gethostbyaddr() example - Chapter 4 - environment.py

import sys, socket

def getipaddrs(hostname):
    """Given a host name, perform a standard lookup and return
        a list of IP addresses for that host."""
    result = socket.getaddrinfo(hostname,None,0, socket.SOCK_STREAM)
    return [ x[4][0] for x in result ]

# Calling gethostname() returns the name of the local machine
hostname = socket.gethostname()
print("Host name: ", hostname)

# Try to get the fully qualified name.
print("Fully-qualified name: ", socket.getfqdn(hostname))

try:
    print("IP addresses:", ','.join(getipaddrs(hostname)))
except socket.gaierror as e:
    print("Could't not get IP addresses:",e)

