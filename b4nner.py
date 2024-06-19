#!/usr/bin/python3

#Banner Grabbing
#Connect to services with FTP, SMTP, SSH, and others to see your banners 

from sys import argv
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.connect((argv[1], int(argv[2])))

print(mySocket.recv(1024))
