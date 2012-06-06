#!/usr/bin/python3

def pand(s):
    return sorted(s) == sorted("123456789")

A = ((1, 1), (1, 0))

def mult(a, b):
    return ((a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[1][0] + a[0][1] * b[1][1]),
            (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[1][0] + a[1][1] * b[1][1]))

assert mult(A, A) == ((2, 1), (1, 1))

memo = {}
def pow(n):
    if n == 1:
        return A
    if n in memo:
        return memo[n]
    
    b = pow(n // 2)
    r = mult(b, b)
    if n % 2 == 1:
        r = mult(r, A)
    memo[n] = r
    return r

assert pow(2) == ((2, 1), (1, 1))

def f(n):
    return pow(n)[0][1]

assert f(7) == 13

atail = 1
btail = 1

i = 2
while True:
    i += 1
    if i % 10000 == 0: print(i)
    x = (atail + btail) % 10**9
    btail = atail
    atail = x

    oktail = pand(str(atail))
    if oktail:
        fib = f(i)

        if pand(str(fib)[:9]):
            print('-------')
            print(i)
            break

