#!/usr/bin/python3

def sumDiv(n):
    s = 1
    for x in range(2, n):
        if x*x > n: break
        if n % x == 0:
            s += x
            if x*x != n: s += n // x
    return s

a = [True] * 28124
abun = []
for i in range(2, 28124):
    if sumDiv(i) > i:
        abun.append(i)
        for x in abun:
            if x + i < len(a):
                a[x + i] = False

print(sum(i for i, val in enumerate(a) if val))

