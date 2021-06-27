# aoc 15 2

inp = "input.txt"

total = 0 # total squarefeet of wrapping paper

ribbon = 0 # feet of ribbon

with open(inp) as data:
    for line in data:
        l, w, h = line.split('x')

        l = int(l)
        w = int(w)
        h = int(h)

        # wrapping paper
        total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)# box surface + slack

        # ribbon
        t = [l, w, h] # get two smallest
        a = min(t)
        t.remove(a)
        b = min(t)

        ribbon += 2*a + 2*b + l*w*h


print(total)
print(f'Ribbon {ribbon}')
