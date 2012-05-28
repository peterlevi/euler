#!/usr/bin/python3

from math import sqrt

def sq(n, x):
    for i in range(-2, +3):
        if n == (x + i)**2:
            return x + i
    return 0

squares = set()
a = 1
prev = 1
while True:
    a += 1
    aa = a*a
    s = sq(2*aa - 1, round(a*sqrt(2)))
    if s: 
        n = (s + 1) // 2
        b = (a + 1) // 2
        print(a, n, b, a / prev)
        prev = a
        if n > 10**12:
            break
        if (a > 100000):
            a = int(a * 5.828427) # we notice this asympthotic ratio between the first several solutions

print('-------')
print(b)
assert b == 756872327473
