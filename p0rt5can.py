#!/usr/bin/python3

from sys import argv
import socket

for port in range(1,65535):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if mySocket.connect_ex((argv[1], port)) == 0:
        banner = mySocket.recv(1024)
        print(port,"- OPEN",banner)
        mySocket.close()
