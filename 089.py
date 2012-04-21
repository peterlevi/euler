#!/usr/bin/python3

from math import ceil

r = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
rr = dict((v, k) for k, v in r.items())  
subs = {1 : 1, 5 : 1, 10 : 1, 50 : 10, 100 : 10, 500 : 100, 1000 : 100}

def r2i(s):
    total = 0
    last = None
    lastSum = 0
    for c in s:
        if c != last:
            if last and r[c] > r[last]: total = total - lastSum
            else: total = total + lastSum
            last = c
            lastSum = r[c]
        else:
            lastSum += r[c]
    total += lastSum
    return total

assert r2i('XIIII') == 14
assert r2i('XIV') == 14
assert r2i('VVIV') == 14
assert r2i('XIX') == 19
assert r2i('CD') == 400
assert r2i('XXC') == 80

def upper(i):
    return min(v for v in r.values() if v >= i)

def lower(i):
    return max(v for v in r.values() if v <= i)

def closest(i):
    u = upper(i)
    l = lower(i)
    if u - i <= subs[u]: return u
    else: return l

assert upper(800) == 1000
assert lower(800) == 500
assert closest(800) == 500
assert upper(200) == 500
assert lower(200) == 100
assert closest(200) == 100
assert upper(6) == 10
assert lower(6) == 5
assert upper(5) == lower(5) == closest(5) == 5

def i2r(i):
    roman = ""
    while i > 1000:
        roman += 'M'
        i -= 1000
    while i > 0:
        c = closest(i)
        if c == i:
            roman += rr[c]
            i -= c
        elif c > i:
            roman += rr[subs[c]] * ceil((c - i) / subs[c])
            roman += rr[c]
            i -= c - subs[c] * ceil((c - i) / subs[c])
        else:
            roman += rr[c]
            i -= c
    return roman

#for i in range(1, 1000):
#    print(i, i2r(i))

assert i2r(49) == 'XLIX'
assert i2r(365) == 'CCCLXV'
assert i2r(848) == 'DCCCXLVIII'

saved = 0
with open('089_roman.txt') as f:
    for s in f:
#        print(s.strip(), i2r(r2i(s.strip())))
        saved += len(s.strip()) - len(i2r(r2i(s.strip())))

#print('-----')
print(saved)
