from functools import reduce
from operator import mul

f = open(0)

sum = 0

for g in f:
    res = {"red": 0, "green": 0, "blue": 0}
    id = int(g.split(": ")[0].split(" ")[1])
    g = g.strip().split(": ")[1].split("; ")
    for s in g:
        a = {"red": 0, "green": 0, "blue": 0}
        for r in s.split(", "):
            n, c = r.split(" ")
            a[c] = int(n)

        for i in a.items():
            res[i[0]] = max(res[i[0]], i[1])

    sum += reduce(mul, res.values(), 1)

print(sum)
