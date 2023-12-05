f = open(0).read().split('\n\n')

seeds = list(map(int, f[0].split(': ')[1].split()))
rules = [f[r].split('map:\n')[1].strip().split('\n') for r in range(1, len(f))]

res = []

for s in seeds:
    for r in rules:
        for row in r:
            x, y, z = map(int, row.split())
            if y <= s < y + z:
                s = s - y + x
                break
    res.append(s)

print(min(res))

