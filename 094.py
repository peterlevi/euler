#!/usr/bin/python3

import math

def sq(n):
    x = round(math.sqrt(n))
    if x*x == n:
        return x
    return 0

def ok(a, d):
    s = (3*a + d)*(a + d)*(a + d)*(a - d)
    x = sq(s)
    return x != 0 and x % 4 == 0

assert ok(5, 1)
assert not ok(6, 0)

s = 0
i = 0
prev = 1
while i <= 10**9 // 3:
    i += 1
    if ok(i, -1):
        print(i, i, i-1)
        s += 3*i - 1
        print(i / prev) # we notice an assymptotic ratio between consecutive solutions - 3.73205...
        prev = i
        if i > 100000:
            i = int(3.73 * i)
    if ok(i, +1):
        print(i, i, i+1)
        s += 3*i + 1
        print(i / prev)
        prev = i
        if i > 100000:
            i = int(3.73 * i)
print('------')
print(s)
