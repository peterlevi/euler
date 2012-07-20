#!/usr/bin/python

import primes
import itertools

p = list(primes.primes_sieve(120000))

def factors(n):
    if n <= 1:
        return []
    f = 0
    r = []
    while p[f] <= n:
        isf = False
        while n % p[f] == 0:
            isf = True
            n //= p[f]
        if isf: r.append(p[f])
        f += 1
    return r

def solve(limit, cnt):
    a = [True] * (limit + 1)
    a[0] = a[1] = False
    cnt -= 1
    while True:
        for i, v in enumerate(a):
            if v:
                c = factors(i)
                break
        #print c
        x = []
        for prime in c:
            x.append(range(1, 17))
        numbers = []
        for pows in itertools.product(*x):
            z = 1
            for i, p in enumerate(pows):
                z *= c[i] ** p
            numbers.append(z)
        numbers = sorted(numbers)
        #print numbers
        for x in numbers:
            if x <= limit:
                a[x] = False
                cnt -= 1
                if cnt == 0:
                    return x
            
print solve(100000, 10000)

