lines = open("input").readlines()

map = [(0, 0)]
map2 = [(0, 0)]

dict = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1),
}

for i in range(0, len(lines[0]), 2):
    c = lines[0][i]
    r = lines[0][i + 1]
    map.append((map[-1][0] + dict[c][0], map[-1][1] + dict[c][1]))
    map2.append((map2[-1][0] + dict[r][0], map2[-1][1] + dict[r][1]))

res = map + map2

print(len(set(res)))
