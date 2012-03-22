#!/usr/bin/python3

def find():
    for a in range(9, -1, -1):
        for b in range(9, -1, -1):
            for c in range(9, -1, -1):
                number = 100001*a + 10010*b + 1100*c
                r = ok(number)
                if r:
                    print(number, r[0], r[1])
                    return

def ok(x):
    for d in range(999, 99, -1):
        if x % d == 0 and x / d >= 100 and x / d <= 999:
            return d, x / d
    return False

find()

