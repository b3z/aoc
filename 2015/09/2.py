import networkx as nx
from itertools import permutations

lines = open("input").read().splitlines()

g = nx.Graph()

for l in lines:
    r = l.split(' ')
    g.add_edge(r[0], r[2], weight=int(r[-1]))

perms = permutations(g.nodes)

max = 0
for p in perms:
    res = nx.path_weight(g, path=p, weight='weight')
    if res > max:
        max = res
print(max)
