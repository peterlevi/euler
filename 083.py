#!/usr/bin/python3

m = []
with open('082_matrix.txt') as f:
    for l in f:
        m.append(list(map(int, l.split(','))))

m_test = [[131, 673, 234, 103, 18],
    [201, 96,  342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37,  331]]         

def solve(m):
    best = [[10**10] * len(m[0]) for i in range(len(m))]
    best[0][0] = m[0][0]
    unvisited = set((i, j) for i in range(len(m)) for j in range(len(m[0])))
    while True:
        (d, ci, cj) = min((best[i][j], i, j) for (i, j) in unvisited)
        unvisited.remove((ci, cj))
        if (ci, cj) == (len(m) - 1, len(m[0]) - 1):
            return d
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i = ci + direction[0]
            j = cj + direction[1]
            if i >= 0 and i < len(m) and j >= 0 and j < len(m[0]):
                best[i][j] = min(best[i][j], d + m[i][j])

assert solve(m_test) == 2297
ans = solve(m)
print(ans)
assert ans == 425185  
