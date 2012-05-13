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
    best = [[0] * len(m[0]) for i in range(len(m))]
    for j in range(len(m[0])):
        for i in range(len(m)):
            if j == 0:
                best[i][j] = m[i][j]
            else:
                if i == 0:
                    best[i][j] = best[i][j-1] + m[i][j]
                else:
                    best[i][j] = min(best[i-1][j], best[i][j-1]) + m[i][j]
                    for k in range(i - 1, -1, -1):
                        best[k][j] = min(best[k][j], m[k][j] + best[k + 1][j])
                   
    return min(best[i][-1] for i in range(len(m)))

assert solve(m_test) == 994
ans = solve(m)
assert ans == 260324
print(ans)
