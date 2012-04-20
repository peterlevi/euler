#!/usr/bin/python3

def isPrime(n):
    for i in range(2, n):
        if i*i > n:
            return True
        if n % i == 0:
            return False

def normalize(n):
    return int("".join(sorted([c for c in str(n)])))

assert isPrime(1487) and isPrime(4817) and isPrime(8147)

f = {}
for n in range(1000, 10000):
    if isPrime(n):
        f.setdefault(normalize(n), []).append(n)
for k, v in f.items():
    if len(v) >= 3:
        for a in v:
            for b in v:
                for c in v:
                    if a < b and b - a == c - b:
                        print(a, b, c)

