#!/usr/bin/python3

MOD = 10**10

def pow(a, n):
    if n == 0:
        return 1
    s = 1
    p = a
    while 2*s <= n:
        p = p*p % MOD
        s *= 2
    return p * pow(a, n - s) % MOD

print(28433 * pow(2, 7830457) % MOD + 1)
