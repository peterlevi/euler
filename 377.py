#!/usr/bin/python

from numpy import *
from numpy.linalg import *

MOD = 1000000000

def partition(sumDigits, maxDigit, count, prefix):
    if count == 1:
        if 1 <= sumDigits <= maxDigit:
            yield prefix + (sumDigits,)
        else:
            return
    for d in range(1, min(maxDigit + 1, sumDigits + 1)):
        gen = partition(sumDigits - d, d, count - 1, prefix + (d,))
        for x in gen:
            yield x


def calcSum(p):
    k = 1
    for i in range(2, len(p) + 1):
        k *= i
    prev = -1
    cnt = 1
    for d in p:
        if d == prev:
            cnt += 1
        else:
            cnt = 1
        k //= cnt
        prev = d

    k *= sum(p)
    k /= len(p)
    ones = 1
    for i in range(len(p) - 1):
        ones = ones * 10 + 1
   
    return k * ones


assert sum(calcSum(p) for i in range(1, 6) for p in partition(5, 5, i, ())) == 17891
sum13 = sum(calcSum(p) for i in range(1, 14) for p in partition(13, 9, i, ())) % MOD
assert sum13 == 856884757

A = matrix(
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0]
    ])

Neg = matrix(
   [[ 0,  1,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  1,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  1,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  1,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  1,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  1,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  1,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  1],
    [ 1, -1, -1, -1, -1, -1, -1, -1, -1]])



B = [identity(9)]
for i in range(1, 17+1):
    C = B[-1]
    for j in range(13):
        C = C*A
        for r, row in enumerate(C):
            for c, col in enumerate(row):
                C[r, c] %= MOD
    B.append(C)

Negs = [identity(9), Neg]
for i in range(2, 81+1):
    Negs.append(Negs[-1]*Neg)

V = matrix([1, 0, 0, 0, 0, 0, 0, 0, 0]).T

def g(n, i):
    print(B[i])
    print(13**i - n)
    print(Negs[13**i - n])
    print(B[i]*Negs[13**i - n])
    return int(round((B[i]*Negs[13**i - n])[0, 0])) % MOD
assert g(5, 1) == 16
assert g(13, 1) == 4076
print(g(133, 2))
exit()

finalSum = sum13
for i in range(2, 17+1):
    print(i)
    pow = 13 ** i
    for sumDigits in range(9, 82):
        gg = g(pow - sumDigits, i)
        print(sumDigits, pow-sumDigits, gg)
        for p in partition(sumDigits, 9, 9, ()):
            if len(p) == 9:
                finalSum = (finalSum + calcSum(p) * gg) % MOD


print(finalSum)
