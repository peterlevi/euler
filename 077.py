#!/usr/bin/python3

import primes

pr = list(primes.primes_sieve(1000))

a = {}
def calc(s, m): # how many ways to get sum s using terms less than or equal to m
    if s < 0 or s == 1:
        return 0
    if s == 0:
        return 1
    if (s,m) in a:
        return a[(s,m)]
    else:
        t = 0
        for p in pr:
            if p > m or p > s:
                break
            t += calc(s - p, p)
        a[(s,m)] = t
        return a[(s, m)]

assert calc(10, 10) == 5

n = 2
while calc(n, n) <= 5000:
    n += 1
print(n)
assert n == 71
