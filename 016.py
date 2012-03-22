#!/usr/bin/python3
x = 1 
for i in range(1000): x *= 2
sum = 0
for c in str(x): sum += int(c)
print(sum)

