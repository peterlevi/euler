#!/usr/bin/python3
#from string import split
import math

f = open('011.data', 'r')
a = [line.split() for line in f]


dirs = [(a, b) for a in range(-1, 2) for b in range(-1, 2) if a != 0 or b != 0]

def calc(x, y, d):
    try:
        p = 1
        for i in range(4):
            p = p * int(a[x + i * d[0]][y + i * d[1]])
        return p
    except IndexError:
        return 0

maxp = 0

print(dirs)
for d in dirs:
    for x in range(len(a)):
        for y in range(len(a[x])):
            maxp = max(maxp, calc(x, y, d))

print(maxp)

