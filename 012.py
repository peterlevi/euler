#!/usr/bin/python
from gmpy import mpz

smallPrimes = [2]
while len(smallPrimes) < 30:
        smallPrimes.append(int(mpz(smallPrimes[-1]).next_prime()))

def cnt(x):
    p = 1

    for d in smallPrimes:
        count = 1
        if d * d > x: 
            break
        while x % d == 0: 
            count += 1
            x //= d
        if d == 2 and count > 1: count -= 1
        p *= count
    else: 
        raise Exception('Not enough primes')
    if x > 1:
        p *= 2

    return p

n = 1 
while cnt(n) * cnt(n + 1) < 500: n += 1
print(n * (n + 1) // 2)

