from functools import reduce
import operator

lines = open("input").readlines()

res = 0

for line in lines:
    s = sorted(map(int, line.split("x")))
    wrap = s[0] * 2 + s[1] * 2
    bow = reduce(operator.mul, s)
    res += wrap + bow

print(res)
