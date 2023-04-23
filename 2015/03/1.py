lines = open("input").readlines()

map = [(0, 0)]

dict = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1),
}

for c in lines[0]:
    map.append((map[-1][0] + dict[c][0], map[-1][1] + dict[c][1]))

print(len(set(map)))
