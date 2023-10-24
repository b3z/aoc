# Incredibly slow solution. This solution took 54 min to compute. Lol.
import datetime

t = datetime.datetime.now()
file = open("input").read().splitlines()

grid = []
y_max = 0

sandStart = (500, 0)
xs, ys = sandStart
res = 0

def genRange(a, b):
    if a - b > 0:
        return range(a, b, -1)
    else:
        return range(a, b, 1)


for line in file:
    points = line.strip().split(" -> ")
    tmp = []
    for i, p in enumerate(points):
        x, y = list(map(int, p.split(",")))

        y_max = max(y_max, y)

        if i >= len(points) - 1:
            tmp += [(x, y)]
            continue

        xn, yn = list(map(int, points[i + 1].split(",")))

        if x == xn:
            tmp += [(x, s) for s in genRange(y, yn)]
        else:
            tmp += [(s, y) for s in genRange(x, xn)]

    grid += tmp

grid = set(grid)

# Simulate


def fall(xs, ys):
    while True:
        if (xs, ys + 1) not in grid and ys < y_max+1:  # Straight down
            ys += 1
            # if ys > y_max + 2:
            #     return None
            continue
        if (xs - 1, ys + 1) not in grid and ys < y_max+1:  # Left
            xs -= 1
            ys += 1
            continue
        if (xs + 1, ys + 1) not in grid and ys < y_max+1:  # Right
            xs += 1
            ys += 1
            continue
        break

    if (xs, ys) == sandStart:
        return None

    return (xs, ys)


while True:
    r = fall(xs, ys)

    if r:
        xs, ys = r
    else:
        print(res+1)
        break
    grid.add((xs, ys))
    res += 1
    xs, ys = sandStart

print('Time to process:' ,datetime.datetime.now()-t)
