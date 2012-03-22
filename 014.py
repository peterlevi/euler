#!/usr/bin/python3

lens = {}
lens[1] = 1
best = (1, 1)

def calc(n):
    global best
    global lens
    m = n
    cnt = 0
    while True:
        cnt += 1
        if n % 2 == 0: n //= 2
        else: n = 3 * n + 1
        if n in lens:
            lens[m] = lens[n] + cnt
            if lens[m] > best[0]:
                best = (lens[m], m)
            return lens[m]


for n in range(1, 1000000): calc(n)
print(best)                

