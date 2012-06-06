#!/usr/bin/python3

def pos(x1, y1, x2, y2):
    c = y1*(x1-x2) - x1*(y1-y2)
    if c > 0: return 1
    elif c < 0: return -1
    return 0

def ok(x1, y1, x2, y2, x3, y3):
    p1, p2, p3 = pos(x1, y1, x2, y2), pos(x2, y2, x3, y3), pos(x3, y3, x1, y1)
    return (p1 >= 0 and p2 >= 0 and p3 >= 0) or (p1 <= 0 and p2 <= 0 and p3 <= 0)

assert ok(-340,495,-153,-910,835,-947)
assert not ok(-175,41,-421,-714,574,-645)

c = 0
with open("102_triangles.txt") as f:
    for l in f:
        arr = map(int, l.split(','))
        if ok(*arr):
            c += 1
print(c)
assert c == 228

