#!/usr/bin/python

a = [[0]*21 for x in range(21)]

def c(x, y):
    if x == 0 or y == 0:
        return 1
    if a[x][y] == 0:
        a[x][y] = c(x - 1, y) + c(x, y - 1)
    return a[x][y]

print(c(20,20))

