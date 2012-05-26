#!/usr/bin/python3

def triple(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b == c or a + c == b or b + c == a)

MAX = 51
s = 0
for x1 in range(0, MAX):
    for x2 in range(x1, MAX):
        for y1 in range(0, MAX):
            for y2 in range(0, y1 + 1):
                if triple(x1**2 + y1**2, x2**2 + y2**2, (x1-x2)**2 + (y1-y2)**2):
                    s += 1

print(s)                    
