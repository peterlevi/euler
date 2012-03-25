#!/usr/bin/python3

digits = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}
special = {10 : "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
           20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

def gen(n):
    if n == 1000:
        return "one thousand"
    s = ""
    if n // 100 > 0:
        s += digits[n // 100] + " hundred"
        n %= 100
        if n > 0: s += " and "
    if n in special:
        s += special[n]
    else:
        if n // 10 > 0:
            s += special[n // 10 * 10]
            if n % 10 > 0:
                s += " "
        if n % 10 > 0:
            s += digits[n % 10]
    return s

assert gen(1) == "one"
assert gen(10) == "ten"
assert gen(23) == "twenty three"
assert gen(100) == "one hundred"
assert gen(110) == "one hundred and ten"
assert gen(123) == "one hundred and twenty three"
assert gen(1000) == "one thousand"

def cnt(s): return sum([1 for c in s if c != ' '])
assert cnt(gen(10)) == 3
assert cnt(gen(23)) == 11
assert cnt(gen(100)) == 10

t = 0
for n in range(1, 1001):
    t += cnt(gen(n))
print(t)