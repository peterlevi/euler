#!/usr/bin/python3

def cycle(n):
    d = []
    used = {}
    x = 1
    i = 1
    while x < n:
        x *= 10
    while True:
        if x in used: break
        used[x] = True
        d.append(x // n)
        x %= n
        x *= 10
        i += 1
        if x == 0: 
            return (0, d)
        while x < n:
            d.append(0)
            x *= 10
    return(len(d), d)

assert cycle(7)[0] == 6
assert cycle(81)[0] == 9
assert cycle(3)[0] == 1
assert cycle(4)[0] == 0
assert cycle(25)[0] == 0

m = 0
md = 0
for d in range(2, 1000):
    if cycle(d)[0] > m:
        m = cycle(d)[0]
        md = d
print(md)
