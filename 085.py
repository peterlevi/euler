#!/usr/bin/python3

print(min((abs(x*y*(x+1)*(y+1)//4 - 2000000), x, y, x*y*(x+1)*(y+1)//4, x*y) for x in range(1500) for y in range(1500)))
