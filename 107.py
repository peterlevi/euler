#!/usr/bin/python3

def mst(m):
    v = set([0])
    u = set(range(1, len(m)))
    edges = set()
    while u:
        e = min((m[x][y], x, y) for x in v for y in u)
        edges.add(e)
        v.add(e[2])
        u.remove(e[2])

    return edges

assert sum(e[0] for e in mst([[0, 25, 10, 5], [25, 0, 10000, 20], [10, 10000, 0, 15], [5, 20, 15, 0]])) == 35

m = []
with open("107_network.txt") as f:
    for l in f:
        m.append(list(map((lambda s: 10**9 if s == '-' else int(s)), l.strip().split(','))))

s = mst(m)
total = sum(x for l in m for x in l if x < 10**9) // 2
best = sum(e[0] for e in s)
assert best == 2153
print(total - best)
