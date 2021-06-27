# aoc 15 2

inp = "input.txt"

total = 0 # total squarefeet of wrapping paper

with open(inp) as data:
    for line in data:
        l, w, h = line.split('x')

        l = int(l)
        w = int(w)
        h = int(h)

        total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)# box surface + slack

print(total)

