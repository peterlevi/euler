#!/usr/bin/python

def ok1(a):
    for i in xrange(2, len(a)):
        if sum(a[:i]) <= sum(a[-(i - 1):]):
            return False
    return True

def ok2(a):
    sums = set([0])
    for x in a:
        for s in list(sums):
            if x + s in sums:
                return False
            sums.add(x + s)
    return True

def ok(a):
    a = sorted(a)
    return ok1(a) and ok2(a)

assert ok([1])
assert ok([1, 2])
assert ok([2, 3, 4])
assert ok([3, 5, 6, 7])
assert ok([6, 9, 11, 12, 13])
assert not ok([1,2,3,4,5,6])

assert ok([11,17, 20, 22, 23, 24])
assert ok([11, 18, 19, 20, 22, 25])

s = 0
with open("105_sets.txt") as f:
    for l in f:
        a = sorted(map(int, l.strip().split(',')))
        if ok1(a) and ok2(a):
            s += sum(a)

print s
