from functools import reduce
import operator

inv = []
tmp = []
with open("input") as f:
    f = f.readlines()
    for l in f:
        if l.strip():
            tmp.append(int(l))
        else:
            inv.append(tmp)
            tmp = []

total = []
for i in inv:
    total.append(sum(i))

m = max(total)
print(total.index(m), m)

