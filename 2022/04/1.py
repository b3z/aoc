lines = open("input").readlines()

c = 0

for l in lines:
    a, b = l.replace("\n", "").split(",")
    a = (int(a.split("-")[0]), int(a.split("-")[1]))
    b = (int(b.split("-")[0]), int(b.split("-")[1]))

    if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
        c += 1

print(c)
