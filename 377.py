#!/usr/bin/python

MOD = 1000000000

f = [1, 1]
for i in range(2, 3000):
    f.append(sum(x for x in f[max(0, i - 9):]) % MOD)
#print(f[:100])

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
    if len(p) == 9: k = 362880
    else:
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
    if len(p) == 9: ones = 111111111
    else:
        for i in range(len(p) - 1):
            ones = ones * 10 + 1
   
    return k * ones

assert calcSum((1,1,1,1,1,1,2,2,2)) == 12444444432


assert sum(calcSum(p) for i in range(1, 6) for p in partition(5, 5, i, ())) == 17891

sum13 = sum(calcSum(p) for i in range(1, 14) for p in partition(13, 9, i, ())) % MOD
assert sum13 == 856884757

I = [[0]*9 for _ in range(9)]
for i in range(9):
    I[i][i] = 1

A = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0]
    ]

Neg = [
    [ 0,  1,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  1,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  1,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  1,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  1,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  1,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  1,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  1],
    [ 1, -1, -1, -1, -1, -1, -1, -1, -1]]


def show(A): 
    for row in A: print(row)

def dot(A, B):
    R = [[0]*9 for _ in range(9)] 
    for i in range(9):
        for j in range(9):
            R[i][j] = sum(A[i][k] * B[k][j] for k in range(9)) % MOD
    return R

def power(A, n):
    R = A
    for i in range(n - 1):
        R = dot(R, A)
    return R

B = [I, power(A, 13)]
for i in range(1, 17+1):
    B.append(power(B[-1], 13))

#for b in B: show(b); print(';');

Negs = [I]
for i in range(1, 82):
    Negs.append(dot(Negs[-1], Neg))

def g(n):
    i = 0
    while 13**i < n: i += 1
    return (dot(B[i], Negs[13**i - n])[0][0]) % MOD

assert g(5) == 16
assert g(13) == 4076
assert g(13*13) == f[13*13]
assert g(13*13 - 10) == f[13*13 - 10]
assert g(13**3 - 36) == f[13**3 - 36]


finalSum = sum13
for i in range(2, 17+1):
    print(i)
    pw = 13 ** i
    for sumDigits in range(9, 82):
        gg = g(pw - sumDigits)
        # print(sumDigits, pw - sumDigits, gg)
        for p in partition(sumDigits, 9, 9, ()):
            #print(p)
            finalSum = (finalSum % MOD + (calcSum(p) % MOD) * gg) % MOD


print(finalSum)

assert finalSum == 732385277
