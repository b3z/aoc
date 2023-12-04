f = open(0)

sum = 0

for g in f:
    sx = []
    id = int(g.split(": ")[0].split(" ")[1])
    g = g.strip().split(": ")[1].split("; ")
    for s in g:
        a = {"red": 0, "green": 0, "blue": 0}
        for r in s.split(", "):
            n, c = r.split(" ")
            a[c] = int(n)

        if a["red"] > 12 or a["green"] > 13 or a["blue"] > 14:
            break
    else:
        sum += id

print(sum)
