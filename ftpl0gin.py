#!/usr/bin/python3

import socket
from sys import argv

port = 21

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.connect((argv[1],port))
print(mySocket.recv(1024))

mySocket.send(f"USER {argv[2]}\r\n".encode())
print(mySocket.recv(1024))

mySocket.send(f"PASS {argv[3]}\r\n".encode())
print(mySocket.recv(1024))
