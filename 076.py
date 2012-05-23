#!/usr/bin/python3

a = {}
def calc(s, m): # how many ways to get sum s using terms less than or equal to m
    if s <= 1 or m == 1:
        return 1
    if (s,m) in a:
        return a[(s,m)]
    else:
        a[(s,m)] = sum(calc(s - i, i) for i in range(1, min(s, m) + 1))
        return a[(s, m)]

assert calc(100, 99) == 190569291
print(calc(100, 99))
