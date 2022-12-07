from sys import maxsize

lines = open("input").readlines()

w = {}
tree = {}
help = []

for l in lines:
    l = l.replace("\n", "")
    if l[0] == "$":
        if l[2] == "c":
            if l[5:] == "/":
                w = tree
                help = []
            elif l[5:] == "..":
                w = help.pop()
            else:
                if l[5:] not in w:
                    w[l[5:]] = {}
                help.append(w)
                w = w[l[5:]]
    else:
        x, y = l.split(" ")
        if x == "dir":
            if y not in w:
                w[y] = {}
        else:
            w[y] = int(x)


def smallest(tr):
    #     if type(tree) == int:
    #         return (tree, 0)
    #     sz = 0
    res = maxsize
    ts = calcSize(tr)
    if ts >= (calcSize(tree) - 40000000):
        res = ts
    for t in tr.values():
        if type(t) == int:
            continue
        r = smallest(t)
        res = min(res, r)
    #     if sz <= 100000:
    #         res += sz
    return res


def calcSize(tree):
    if type(tree) == int:
        return tree
    return sum(map(calcSize, tree.values()))


print(smallest(tree))
