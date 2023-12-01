import re

file = open("input")
sum = 0

for f in file:
    a = "".join(re.findall(r"\d+", f))
    sum += int(a[0] + a[-1])

print(sum)
