import socket
from sys import argv

print(f"{argv[1]} --> {socket.gethostbyname(argv[1])}")
