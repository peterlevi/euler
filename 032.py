#!/usr/bin/python3

def perm(n, acc):
    if len(acc) == n:
        yield acc
    for d in range(1, n + 1):
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
print(get(p, 0, 2), get(p, 2, 5), get(p, 5, 9))
assert get(p, 0, 2) * get(p, 2, 5) == get(p, 5, 9)

used = set()
t = 0
for p in perm(9, ()):
    print(p)
    for i in range(1, 5):
        for j in range(i + 1, 8):
            product = get(p, j, 9)
            if get(p, 0, i) * get(p, i, j) == product and not product in used:
                t += product
                used.add(product)

print(t)
assert t == 45228
