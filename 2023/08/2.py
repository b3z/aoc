import math

cc, *mm = open(0).read().splitlines()

grid = {}
for m in mm[1:]:
    t = m.split()
    a = t[0]
    b = t[2][1:-1]
    c = t[3][:-1]
    grid[a] = (b, c)

sp = []
for g in grid:
    if g[-1] == "A":
        sp.append(g)



def find_num(i):
    counter = 0
    while len(sp):
        for c in cc:
            counter += 1
            if c == "R":
                sp[i] = grid[sp[i]][1]
            elif c == "L":
                sp[i] = grid[sp[i]][0]
            else:
                print("error")
                exit()

            if sp[i][-1] == "Z":
                return counter


num = [0] * len(sp)
for i in range(len(sp)):
    num[i] = find_num(i)

res = 1
for n in num:
    res *= n // math.gcd(res, n)

print(res)
