#!/usr/bin/python3

MOD = 1000000

p = [0] * 1000000
p[0] = 1

n = 0
while True:
    n += 1
    sign = -1
    s = 0
    for k in range(1, n + 1):
        sign = -sign
        i1 = n - k * (3*k - 1) // 2
        i2 = n - k * (3*k + 1) // 2
        v1 = 0 if i1 < 0 else p[i1]
        v2 = 0 if i2 < 0 else p[i2]
        s += sign * (v1 + v2)
        s = s % MOD
        if i1 < 0:
            break
    p[n] = s
    if s == 0:
        print(n)
        assert n == 55374
        break
