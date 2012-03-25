#!/usr/bin/python2
import math

def cnt(x):
    s = 0
    for d in xrange(2, int(round(math.sqrt(x))) + 1):
        if x % d == 0:
            s += d
            if x // d != d: s += x // d
    return s + 1

cnts = [0, 0]
for i in xrange(2, 30000):
    cnts.append(cnt(i))

sum = 0
for i in xrange(2, 10000):
    if i != cnts[i] and cnts[cnts[i]] == i:
#        print(i, cnts[i])
        sum += i

print(sum)
