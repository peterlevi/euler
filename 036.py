#!/usr/bin/python3

def isPal(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

assert isPal('aabbabbaa')
assert isPal('aabbaabbaa')
assert not isPal('abca')

print(sum(i for i in range(1, 1000000) if isPal(str(i)) and isPal("{0:b}".format(i))))

