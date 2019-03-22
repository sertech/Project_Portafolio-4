#!/usr/bin/env python3

import socket

HOST = '192.168.1.28'  # Standard loopback interface address (localhost)
PORT = 9999        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #socket.socket() creates a socket object that supports the context manager type, so you can use it in a with statement. There’s no need to call s.close()
    s.bind((HOST, PORT))
    s.listen() # listen() enables a server to accept() connections. It makes it a “listening” socket
    conn, addr = s.accept() # it's imperative to understand is that we now have a new socket object from accept()
    '''
    client socket object = conn
    accept() blocks and waits for an incoming connection. When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client. The tuple will contain (host, port) for IPv4 connections or (host, port, flowinfo, scopeid) for IPv6. See Socket Address Families in the reference section for details on the tuple values. 
    '''
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: # If conn.recv() returns an empty bytes object, b'', then the client closed the connection and the loop is terminated. 
                break
            print('Received RFID CODE', repr(data))
            conn.sendall(data)
        


'''
import socket

HOST = '192.168.1.28'  # The server's hostname or IP address
PORT = 9999        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
'''
