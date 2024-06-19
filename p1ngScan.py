#!/bin/python3

import os
from sys import argv

for i in range(1,254):
    os.system(f"ping -c 1 {argv[1]}.{i} | grep '64 bytes'")
