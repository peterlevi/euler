#!/usr/bin/python

import primes
import math

from operator import mul

def prod(l):
    return reduce(mul, l)

target = 4000000 * 2 - 1
maxprimes = int(math.ceil(math.log(target, 3)))

g = primes.primes()
p = []
for i in xrange(maxprimes):
    p.append(next(g))

def solutions(ks):
    return prod(map(lambda k: 2*k + 1, ks)) 

def valid(ks):
    return sorted(ks, reverse = True) == ks and \
        solutions(ks) >= target

SOL = [3,3,2,2,1,1,1,1,1,1,1,1]
assert valid(SOL)

def getn(ks):
    r = 1
    for i, k in enumerate(ks):
        r *= p[i] ** k
    return r

assert getn(SOL) == 9350130049860600

def factors(n, f = 0):
    c = 0
    if n <= 1:
        return []
    while n % p[f] == 0:
        c += 1
        n //= p[f]
    return [c] + factors(n, f + 1)

facts = map(factors, list(xrange(p[-1] + 1)))

def add(ks, factors):
    if len(factors) > len(ks):
        return ks
    dup = list(ks)
    for i, x in enumerate(factors):
        dup[i] += x
    return dup

ks = [1] * maxprimes
while True:
    print ks
    last = list(ks)
    limit = p[len(ks) - 1]
    print limit
    ks[-1] -= 1
    assert not valid(ks)
    for i in xrange(2, limit):
        test = add(ks, facts[i])
        print "testing ", i, test, solutions(test), valid(test)
        if valid(test):
            ks = test
            ks = [k for k in ks if k > 0]
            break
    else:
        break
print "------------"
print last
print getn(last)
    
