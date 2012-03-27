#!/usr/bin/python3

digs = list(range(0, 10))
n = 9
nfact = 362880 # 9!
t = 999999
while n > 0:
    print(digs[t // nfact], end='')
    del digs[t // nfact]
    t %= nfact
    nfact //= n
    n -= 1
print(digs[0])
