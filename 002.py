def fib(max):
    a = 1
    b = 1
    while a <= max:
        yield a
        b += a
        a = b - a

print(sum(x for x in fib(4000000) if x % 2 == 0))
