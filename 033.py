#!/usr/bin/python

pairs = [(x*10+ z, z*10 + y) for x in range(1, 10) for y in range(1, 10) for z in range(0, 10) if x*(10*z + y) == y*(10*x + z) and x != y]
p = 1
d = 1
assert len(pairs) == 4

for x, y in pairs:
    p *= x
    d *= y

def gcd(x, y):
    if x == 0: return y
    if y == 0: return x
    if x > y: 
        return gcd(x - y, y)
    else:
        return gcd(x, y - x)


assert gcd(8, 20) == 4

print d // gcd(p, d)
