#!/usr/bin/python3

def isPrime(x):
    if x < 2: 
        return False
    for i in range(2, x//2 + 1):
        if i**2 > x:
            break
        if x % i == 0:
            return False
    return True

assert isPrime(3)
assert not isPrime(4)
assert isPrime(11)

def isOk(x):
    m = x
    while m >= 1:
        if not isPrime(m):
            return False
        m = m // 10
    m = x
    while m >= 1:
        if not isPrime(m):
            return False
        if m >= 10:
            m = int(str(m)[1:])
        else:
            m = 0
    return True

c = 0
s = 0
n = 10
while c < 11:
    n += 1
    if isOk(n):
        print(n)
        c += 1
        s += n

print('---------')
print(s)

