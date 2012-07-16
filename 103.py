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

best = [20, 20+11, 20+18, 20+19, 20+20, 20+22, 20+25]
limit = sum(best) + 1

for a in xrange(17, limit):
    for b in xrange(a + 1, (limit - a) // 6):
        for c in xrange(b + 1, (limit - (a+b)) // 5):
            for d in xrange(c + 1, (limit - (a+b+c)) // 4):
                for e in xrange(d + 1, (limit - (a+b+c+d)) // 3):
                    for f in xrange(e + 1, (limit - (a+b+c+d+e)) // 2):
                        for g in xrange(f + 1, limit - (a+b+c+d+e+f)):
                            l = [a,b,c,d,e,f,g]
                            if ok1(l) and ok2(l):
                                print sum(l), l
                                if sum(l) < sum(best):
                                    best = l

print "------"
print "".join(map(str, best))

