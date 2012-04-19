#!/usr/bin/python
from gmpy import mpz

smallPrimes = [2]
while len(smallPrimes) < 10000:
    smallPrimes.append(int(mpz(smallPrimes[-1]).next_prime()))

def solve(x):
    f = [set(), set()]
    for n in xrange(2, 100000000):
        for p in smallPrimes:
            if n % p == 0:
                f.append(f[n // p].copy())
                f[-1].add(p)
                break
        else:
            f.append(set())

        if n > 100:
            for i in xrange(x):
                if len(f[n - i]) < x: 
                    break
            else:
                return n - x + 1

assert solve(3) == 644

s = solve(4)
print(s)
assert s == 134043

