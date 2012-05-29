#!/usr/bin/python

def split(n, m = 2, acc = []):
    if n == 1:
        yield acc
        return
    for i in range(m, n + 1):
        if n % i == 0:
            gen = split(n // i, i, acc + [i])
            for s in gen:
                yield s

a = {}
i = 2
for i in range(2, 24000):
    if i % 1000 == 0: 
        print(i)
    for s in split(i):
        k = i - sum(s) + len(s)
        a[k] = min(i, a.setdefault(k, 10**9))

print('-----')
print(sum(set(a[k] for k in range(2, 12001))))


