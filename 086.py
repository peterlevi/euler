#!/usr/bin/python3

from math import sqrt

def cnt(a):
    s = 0
    for b in range(2, 2*a + 1):
        if sq(a**2 + b**2):
            s += allot(a, b)
    return s

def allot(a, b):
    x = b - 2
    m = a - 1
    if x <= m: return x // 2 + 1
    else: return (2*m - x) // 2 + 1

def sq(n):
    return n == round(sqrt(n))**2

assert allot(6, 8) == 3
assert allot(6, 12) == 1
assert allot(6, 3) == 1
assert allot(6, 6) == 3
assert allot(6, 7) == 3

assert sum(cnt(a) for a in range(1, 100)) == 1975

s = 0
m = 0
while s <= 1000000:
    m += 1
    s += cnt(m)
print(m)
