#!/usr/bin/python

def fact(n):
    p = 1
    for i in xrange(2, n + 1):
        p *= i
    return p

def c(n, k):
    return fact(n) // fact(k) // fact(n-k)

assert c(6, 4) == 15

def subsets(a):
    subs = [[]]
    for x in xrange(1, a + 1):
        for s in list(subs):
            subs.append(s + [x])
    return subs

def halves(a):
    return [x for x in subsets(a) if len(x) == a // 2 and x[0] == 1]

def ok(halve, a):
    for i, x in enumerate(reversed(halve)):
        if i + 1 > (a - x + 1) / 2:
            return True
    return False

def cnt(n): 
    return sum(1 for x in halves(n) if ok(x, n))

def solve(n):
    s = 0
    for k in xrange(4, n + 1, 2):
        s += c(n, k) * cnt(k)
    return s

print solve(12)
