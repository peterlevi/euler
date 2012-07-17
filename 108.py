#!/usr/bin/python

def c(n):
    z = n*n
    return sum(1 for x in xrange(1, n + 1) if z % x == 0)

for i in xrange(60, 200000, 60):
    if c(i) > 1000:
        print i
        break
