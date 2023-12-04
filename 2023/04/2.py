f = open(0).read().splitlines()

sc = [1]*len(f)

for l in f:
    inp = l.split(": ")
    id = int(inp[0].strip().split()[1])
    win, my = [list(map(str, r.split())) for r in inp[1].strip().split(" | ")]
    t = 0

    for m in my:
        if m in win:
            t += 1

    for i in range(id+1, id+t+1):
        if i < len(f)+1:
            sc[i-1] += sc[id-1]

print(sum(sc))

