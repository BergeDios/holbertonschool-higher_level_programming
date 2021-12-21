#!/usr/bin/python3
for n in range(0,100):
    if n in range(0,99):
        print("{:02d}, ".format(n), end='')
    elif n==99:
        print("{:02d}".format(n))
