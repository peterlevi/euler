#!/usr/bin/python3

# Pell's equation x^2 - Dy^2 = 1
# Solution is given by some hi, ki, where hi/ki are the convergents of the continued fraction for sqrt(D)

import math

def nextFrac(a, b, c):
    x = math.sqrt(a)
    d = math.floor((x + b) / c)
    b1 = d*c - b
    c1 = (a - b1**2) / c
    return (d, a, b1, c1)

def frac(a):
    b = 0
    c = 1
    while True:
        (d, a, b, c) = nextFrac(a, b, c)
        yield d

def okPell(D, x, y):
    return x**2 - D*y**2 == 1

def solve(d):
    h1 = 1
    h2 = 0
    k1 = 0
    k2 = 1
    for a in frac(d):
        h = a*h1 + h2
        k = a*k1 + k2
        if okPell(d, h, k):
            return (h, k)
        h2 = h1
        h1 = h
        k2 = k1
        k1 = k

print(max((solve(d), d) for d in range(2, 1001) if d != round(math.sqrt(d))**2))
