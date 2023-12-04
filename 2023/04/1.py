res = 0

for l in open(0):
    win, my = [list(map(str, r.split())) for r in l.split(": ")[1].strip().split(" | ")]
    t = 0

    for m in my:
        if m in win:
            if t == 0:
                t = 1
            else:
                t *= 2
    res += t

print(res)
