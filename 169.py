#!/usr/bin/python3

memo = {}

def f(n, ones):
    if n == 0: 
        return 1

    if n == 1: 
        return 1 if ones else 0
    
    if (n, ones) in memo:
        return memo[(n, ones)]

    result = 0
    if not ones:
        if n % 2 == 1: 
            result = 0
        else: 
            result = f(n // 2, True)
    else:
        if n % 2 == 0: 
            result = f(n - 2, False) + f(n, False)
        else: 
            result = f(n - 1, False)
    memo[(n, ones)] = result
    return result

assert f(10, True) == 5
print(f(10**25, True))
