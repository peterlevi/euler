#!/usr/bin/python3

a = [i for i in range(0, 200000)]

def nextPrime(prevPrime):
    for x in range(prevPrime * prevPrime, len(a), prevPrime):
        if x < len(a):
            a[x] = 0
    for i in range(prevPrime + 1, 200000):
        if a[i] != 0:
            return a[i]

prime = 2
for i in range(10000):
    prime = nextPrime(prime)

print(prime)