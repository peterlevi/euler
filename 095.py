#!/usr/bin/python2
import math

def cnt(x):
    s = 0
    for d in xrange(2, int(round(math.sqrt(x))) + 1):
        if x % d == 0:
            s += d
            if x // d != d: s += x // d
    return s + 1

#a = map(cnt, range(10**6 + 1))
a = []
with open('095.dat') as f:
    a = map(int, f.read().split(','))
assert a[220] == 284
assert a[284] == 220

def chain(i):
    s = set()
    n = i
    cnt = 1
    curMin = 10**9
    while not n in s:
        s.add(n)
        cnt += 1
        if n < curMin:
            curMin = n
        n = a[n]
        if n > 10**6:
            return (0, 0)
    if n == i:
        return (cnt, curMin)
    else:
        return (0, 0)

assert chain(12496) == (6, 12496)

longest = 0
longestFor = 0
minInLongest = 0
for i in range(2, 10**6 + 1):
    (cnt, curMin) = chain(i)
    if cnt > longest:
        longestFor = i
        longest = cnt
        minInLongest = curMin

print(longestFor, longest, minInLongest)
