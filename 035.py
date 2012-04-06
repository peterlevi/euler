#!/usr/bin/python
from gmpy import mpz

smallPrimes = set([2])
lastPrime = 2
while lastPrime < 1000000:
    p = int(mpz(lastPrime).next_prime())
    smallPrimes.add(p)
    lastPrime = p

def rot(n):
    for i in range(len(str(n))):
        yield n
        n = (n % 10) * 10**(len(str(n)) - 1) + n // 10

c = 0
for i in smallPrimes:
    for r in rot(i):
        if not r in smallPrimes:
            break
    else:
        c += 1

print(c)
