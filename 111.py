#!/usr/bin/python

import primes

p = list(primes.primes_sieve(10**6))

def isPrime(n):
    if n <= 1: 
        return False
    if n % 2 == 0:
        return n == 2
    for i in xrange(100000):
        if p[i] * p[i] > n:
            return True
        if n % p[i] == 0:
            return False


sss = 0
for d in xrange(0, 10):
    print d
    o = int(str(d) * 10)
    if isPrime(o):
        sss += o
        print o
        continue

    found = set()
    for a in xrange(0, 10):
        for pos in xrange(0, 10):
            c = [d] * pos + [a] + [d] * (9 - pos)
            n = int(''.join(map(str, c)))
            if n >= 10**9 and isPrime(n):
                print n
                found.add(n)

    
    if not found:
        for a in xrange(0, 10):
            for b in xrange(0, 10):
                for posa in xrange(0, 9):
                    for posb in xrange(posa + 1, 10):
                        c = [d] * posa + [a] + [d] * (posb - posa - 1) + [b] + [d] * (9 - posb)
                        n = int(''.join(map(str, c)))
                        if n >= 10**9 and isPrime(n):
                            print n
                            found.add(n)
    if not found:
        print "not found for " + str(d)
    sss += sum(found)

print "--------------"
print sss
