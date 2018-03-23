#! /usr/bin/env python3
# Simple Server - Chapter 1 - server.py

import socket

host = ''  # Bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)      # enable a server to accept connections.
# backlog , it specifies the number of unaccepted connections that the system will allow before refusing new connections.

print("Server is running on port %d; press Ctrl-C to terminate."%port)

while 1:
    clientsocket, clientaddr = s.accept()
    # accept a connection.
    # the socket must be bound to an address and listening for connections.
    clientfile = clientsocket.makefile('rw')
    clientfile.write("Welcome, %s \n"%str(clientaddr))
    clientfile.write("Please enter a string: ")
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters.\n"%len(line))
    clientfile.close()
    clientsocket.close()
