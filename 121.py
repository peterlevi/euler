#!/usr/bin/python3

import math

def p(k, t, m = 1):
    if k == 0:
        return 1
    s = 0
    for a in range(m, t + 1 - (k - 1)):
        s += a*p(k - 1, t, a + 1)
    return s

assert p(0, 4) == 1
assert p(1, 4) == 1 + 2 + 3 + 4
assert p(2, 4) == 1*2 + 1*3 + 1*4 + 2*3 + 2*4 + 3*4
assert p(3, 4) == 1*2*3 + 1*2*4 + 1*3*4 + 2*3*4
assert p(4, 4) == 1*2*3*4

assert sum(p(r, 4) for r in range(0, 4-3 + 1)) == 11

def fact(n):
    p = 1
    for x in range(2, n + 1): p *= x
    return p

def solve(rounds):
    maxred = math.floor(rounds / 2 - 0.4)
    s = sum(p(r, rounds) for r in range(0, maxred + 1))
    i = 1
    f = fact(rounds + 1)
    while f > i * s: i += 1
    return i - 1

assert solve(4) == 10
print(solve(15))
