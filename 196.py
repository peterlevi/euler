#!/usr/bin/python3

import primes

p = list(primes.primes_sieve(8000000))

def t(n):
    return n*(n+1)//2

assert t(8) == 36

def s(n):
    start = t(n - 3) + 1
    end = t(n + 2) + 1
    m = [1] * (end - start)
    neighbours = [0] * (end - start)

    s = 0
    filterPr(start, end, m, p)
    #print(1, sum(1 for x in m if x > 0))
    filterNeigh(n, start, end, m, neighbours)
    #print(2, sum(1 for x in m if x > 0))
    for x in range(t(n - 1) + 1, t(n) + 1):
        if m[x - start] >= 2 or (m[x - start] == 1 and m[neighbours[x - start] - start] >= 2):
                s += x
    return s

def filterPr(start, end, m, pr):
    for p in pr:
        if p*p > end:
            break
        for i in range(start + (p - start % p) % p, end, p):
            if p < i:
                m[i - start] = 0

def filterNeigh(n, start, end, m, neighbours):
    for i in range(-2, 3):
        for j in range(0, n + i):
            lineStart = t(n + i - 1) + 1
            if m[lineStart + j - start] > 0:
                cnt, ne = neigh(n, i, j, m, start)
                m[lineStart + j - start] = cnt
                neighbours[lineStart + j - start] = ne

def neigh(n, i, j, m, start):
    cnt = 0
    ne = 0
    for dx in range(-1 if i > -2 else 0, (1 if i < 2 else 0) + 1):
        for dy in range(-1 if j > 0 else 0, (1 if j < n + i - 1 else 0) + 1):
            if dx == 0 and dy == 0:
                continue
            val = t(n + i - 1 + dx) + 1 + j + dy
            if m[val - start] > 0:
                cnt += 1
                ne = val
    return (cnt, ne)

assert s(10000) == 950007619 
ans = s(5678027) + s(7208785)
print(ans)
assert ans == 322303240771079935
