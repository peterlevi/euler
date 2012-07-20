#!/usr/bin/python

def pal(n):
    return str(n) == str(n)[::-1]

assert pal(121)

limit = 10**8

s = [(0,0)]
total = 0
counted = set()
for x in xrange(1, 10001):
    news = s[-1][1] + x**2
    for p in s:
        t = news - p[1]
        if t <= limit and pal(t) and not t in counted and p[0] < x - 1:
            #print t, p[0], x
            total += t
            counted.add(t)
    s.append((x, news))
print total
