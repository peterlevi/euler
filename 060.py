#!/usr/bin/python3

import primes

pr = primes.primes_array(100000000)

groups = [[]]

def isPr(x):
    if x < 100000000:
        return pr[x]
    else:
        return primes.isPrime(x) 

def okPair(x, y):
    return isPr(x[0]*y[1] + y[0]) and isPr(y[0]*x[1] + x[0])

assert okPair((3, 10), (109, 1000))
assert not okPair((3, 10), (5, 10))

def ok(group, p):
    for x in group:
        if not okPair(x, p): return False
    return True

assert ok([(3, 10), (7, 10)], (109, 1000))
assert not ok([(3, 10)], (5, 10))

def solve():
    print('start')
    o = 10
    for p in primes.primes_sieve(27000):
        if p == 2 or p == 5:
            continue
        while p > o:
            o *= 10 
        for g in groups:
            if ok(g, (p, o)):
                newg = list(g)
                newg.append((p, o))
                groups.append(newg)
                if (len(newg)) >= 5:
                    print(newg, sum(x[0] for x in newg))

solve()
