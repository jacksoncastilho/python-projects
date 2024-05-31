#!/usr/bin/python3

from sys import argv
import socket

meuSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

status = meuSocket.connect_ex((argv[1], int(argv[2])))

if status == 0:
    print("Connected")
else:
    print("Not Connected")
