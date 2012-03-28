#!/usr/bin/python
from gmpy import mpz

primes = set([2])
smallPrimes = [2]
while len(smallPrimes) < 100000:
    p = int(mpz(smallPrimes[-1]).next_prime())    
    smallPrimes.append(p)
    primes.add(p)

def cnt(a, b):
    n = 0
    while n*n + a*n + b in primes: n += 1
    return n

m = 0
mab = (0, 0)
i = 0
while smallPrimes[i] < 1000:
    b = smallPrimes[i]
    i += 1
    for a in range(-999, 1000):
        x = cnt(a, b)
        if x > m:
            m = x
            mab = (a, b)
        x = cnt(a, -b)
        if x > m:
            m = x
            mab = (a, -b)

print(mab[0], mab[1], mab[0] * mab[1])
