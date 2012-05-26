#!/usr/bin/python3

ops = [lambda a,b : a*b, lambda a,b: a+b, lambda a,b: a-b, lambda a,b: a / b]

def perms(s):
    if not s:
        yield []
        return
    for d in s:
        s.remove(d)
        for p in perms(s):
            yield [d] + p
            yield [-d] + p
        s.add(d)


def getx(s):
    i = 1
    while i in s:
        i += 1
    return i - 1

def calc(s):
    result = set()
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                for p in perms(s):
                    try:
                        x = op3(op2(op1(p[0], p[1]), p[2]), p[3])
                        if x == round(x) and x > 0:
                            result.add(x)
                    except ZeroDivisionError:
                        continue
    return result

v = calc(set([1,2,3,4]))
assert len(v) == 31
assert max(v) == 36
assert getx(v) == 28

maxr = 0
best = (0, 0, 0, 0)
for a in range(0, 7):
    for b in range(a + 1, 8):
        for c in range(b + 1, 9):
            for d in range(c + 1, 10):
                r = getx(calc(set([a, b, c, d])))
                if r > maxr:
                    maxr = r
                    best = (a, b, c, d)

ans = "".join(map(str, best))
print(ans)
assert ans == "1258"
