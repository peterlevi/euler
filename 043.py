#!/usr/bin/python3

def perm(n, acc):
    if len(acc) == n:
        yield acc
    for d in range(0, n):
        if not d in acc:
            for p in perm(n, acc +(d,)):
                yield p

assert len(list(perm(5, ()))) == 120

def get(p, i, j):
    r = 0
    for x in p[i:j]: r = r * 10 + x
    return r

assert get((5,4,3,2,1), 1, 3) == 43
p = (3, 9, 1, 8, 6, 7, 2, 5, 4)
assert get(p, 0, 2) * get(p, 2, 5) == get(p, 5, 9)

divs = [2,3,5,7,11,13,17]
t = 0
for p in perm(10, ()):
    if p[0] != 0:
        for i in range(len(divs)):
            if get(p, i + 1, i + 4) % divs[i] != 0:
                break
        else:
            print(p)
            t += get(p, 0, 10)

print(t)

assert t == 16695334890

