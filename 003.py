from math import sqrt

def simplify(x, lastDivisor):
    for i in range(lastDivisor, int(sqrt(x) + 2)):
        if x % i == 0:
            return simplify(round(x / i), i)
    return x

print(simplify(600851475143, 2))
