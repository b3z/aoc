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


total.sort()
total.reverse()

s = total[0] + total[1] + total[2]

print(total)

print(s)
