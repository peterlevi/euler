#!/usr/bin/python3

fs = [
        lambda n: n*(n+1)//2,
        lambda n: n*n,
        lambda n: n*(3*n-1)//2,
        lambda n: n*(2*n-1),
        lambda n: n*(5*n-3)//2,
        lambda n: n*(3*n-2)
]

maps = []
for f in fs:
    m = {}
    maps.append(m)
    n = 0
    while True:
        n += 1
        x = f(n)
        if x >= 10000: break
        if x < 1000: continue
        m.setdefault(x // 100, []).append(x)

def findSolution(endWith, startWith, useMaps, sol):
    if (len(useMaps) == 0):
        if sol[-1] % 100 == endWith:
            print(sum(sol), sol)
        return
    for m in useMaps:
        if startWith in m:
            for x in m[startWith]:
                findSolution(endWith, x % 100, [k for k in useMaps if k != m], sol + [x])

for l in maps[0].values():
    for x in l:
        findSolution(x // 100, x % 100, maps[1:], [x])


