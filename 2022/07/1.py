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


def sumUp(tree):
    if type(tree) == int:
        return (tree, 0)
    sz = 0
    res = 0
    for t in tree.values():
        su = sumUp(t)
        sz += su[0]
        res += su[1]
    if sz <= 100000:
        res += sz
    return (sz, res)


print(sumUp(tree)[-1])
