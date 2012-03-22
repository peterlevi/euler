#!/usr/bin/python3

a = [i for i in range(0, 2000000)]

def nextPrime(prevPrime):
    for x in range(prevPrime * prevPrime, len(a), prevPrime):
        if x < len(a):
            a[x] = 0
    for i in range(prevPrime + 1, 2000000):
        if a[i] != 0:
            return a[i]
    return 0

prime = 2
while prime:
    prime = nextPrime(prime)

print(sum(a) - 1)
