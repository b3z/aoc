cc, *mm = open(0).read().splitlines()

grid = {}
for m in mm[1:]:
    t = m.split()
    a = t[0]
    b = t[2][1:-1]
    c = t[3][:-1]
    grid[a] = (b, c)

x = "AAA"
counter = 0
while 1:
    for c in cc:
        if c == "R":
            x = grid[x][1]
        elif c == "L":
            x = grid[x][0]
        else:
            print("error")
            exit()
        counter += 1

        if x == "ZZZ":
            print(counter)
            exit()
