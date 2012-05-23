import math

def streamfilter (pred, stream):
    for i in stream:
        if pred(i):
            yield i

def ints(n):
    while True:
        yield n
        n = n + 1

def primes():
    nums = ints(2)
    while True:
        prime = next(nums)
        yield prime
        def curfilter(v, p=prime):
            return v % p != 0
        nums = streamfilter(curfilter, nums)

def isPrime(n):
    if n <= 1: 
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, n, 2):
        if i * i > n:
            return True
        if n % i == 0:
            return False

def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def primes_array(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
    return a

