#!/usr/bin/python3

def genSqrt(n):
    sn = str(n)
    if len(sn) % 2 == 1:
        sn = "0" + sn
    c = 0
    p = 0
    while True:
        while len(sn) < 2:
            sn += "0"
        c = 100*c + int(sn[:2])
        sn = sn[2:]
        x = 0
        for d in range(10):
            if d*(20*p + d) <= c:
                x = d
            else:
                break
        yield(x)
        c = c - x*(20*p + x)
        p = 10*p + x
        if c == 0 and len(sn) == 0:
            break

s = 0
for n in range(2, 100):
    if n in set(x**2 for x in range(11)):
        continue
    gen = genSqrt(n)
    for x in range(100):
        s += next(gen)
print(s)
assert s == 40886 

