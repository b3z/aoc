import re

file = open("test").readlines()
f = [list(map(int, re.findall(r"\d+", row))) for row in file]

notset = set()
nc = 0

sx, sy, bx, by = list(zip(*f))
s = [complex(a, b) for a, b in zip(sx, sy)]
b = [complex(a, b) for a, b in zip(bx, by)]

for s, b in zip(s, b):
    distance = s - b
    e = s
    edges = []
    for x in range(4):
        e *= 1j
        edges.append(e)

    for p in range(int(edges[2].imag), int(edges[0].imag)):
        print(p)
    exit()

print(edges)
