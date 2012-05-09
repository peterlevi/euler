#!/usr/bin/python3

import math

def next(a, b, c):
    x = math.sqrt(a)
    d = math.floor((x + b) / c)
    b1 = d*c - b
    c1 = (a - b1**2) / c
    return (d, a, b1, c1)

def cycleLen(a):
    b = 0
    c = 1
    seen = set()
    while True:
        (d, a, b, c) = next(a, b, c)
        if (b, c) in seen:
            return len(seen)
        seen.add((b, c))

assert cycleLen(13) == 5
assert cycleLen(23) == 4

print(sum(1 for n in range(2, 10001) if n != round(math.sqrt(n))**2 and cycleLen(n) % 2 == 1))
