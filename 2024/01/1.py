f = open('input').read().splitlines()

ax = []
bx = []
for r in f:
    a, b = r.replace('   ', ',').split(',')
    ax.append(int(a))
    bx.append(int(b))

ax = sorted(ax)
bx = sorted(bx)

sum = 0
for a, b in zip(ax, bx):
    sum += abs(b-a)

print(sum)

