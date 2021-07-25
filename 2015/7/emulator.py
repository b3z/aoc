
ops = {
    "NOT"       : lambda x, y : ~x & (1<<16)-1, # takes two args, only the first is evaluated
    "AND"       : lambda x, y : x & y,
    "OR"        : lambda x, y : x | y,
    "RSHIFT"    : lambda x, y : x >> y,
    "LSHIFT"    : lambda x, y : x << y
    }

class Int:
    def __init__(self):
        self.val = -99 
    
    def set(self, x):
        self.val = int(x)

    def get(self):
        return self.val

    def __str__(self):
        return f"{self.val}"

def make(cmd):
    global gates
    tmp = cmd.split(" -> ")
    t   = tmp[0].split(' ')

    target = tmp[1].replace("\n", "")
    lt = len(t)

    if lt == 1:
        if t[0].isdecimal():
            f = Int()
            f.set(t[0])
        else:
            if checkRef(t[0]):
                f = t[0]
            else:
                return False # Reference not exisiting yet
    elif lt == 2:
        if t[1].isdecimal():
            k = Int()
            k.set(t[1])
            f = [t[0], k, Int()]
        else:
            if checkRef(t[1]):
                f = [t[0], t[1], Int()]
            else:
                return False# no ref
    else:
        if t[0].isdecimal() is not True:
            if checkRef(t[0]):
                pass
            else:
                return False
        else:
            tmp = Int()
            tmp.set(t[0])
            t[0] = tmp

        if t[2].isdecimal() is not True:
            if checkRef(t[2]):
                pass
            else:
                return False
        else:
            tmp = Int()
            tmp.set(t[2])
            t[2] = tmp

        f =  [t[1], t[0], t[2]]
      #  print(f"{target} = {f}")
    
    gates[target] = f
    return True

def checkRef(g):
    if g in gates:
        return True
    else:
        return False

gates = {}
res = {}

def evg(t):
    if t in res:
        return res[t]

    g = gates[t]

    if type(g) == Int:
        return g.get()
    elif type(g) == str:
        return evg(g)
    else:
        if type(g[1]) == Int:
            x = g[1].get()
        else:
            x = evg(g[1])

        if type(g[2]) == Int:
             y = g[2].get()
        else:
            y = evg(g[2])

        result = ops[g[0]](x, y)
        res[t] = result
        return result

todo = [] # targets todo
with open("input.txt") as data:
    for line in data:
        if make(line) is False:
            todo.append(line)

while len(todo) > 0:
    for line in todo:
        if make(line):
            todo.remove(line)
        
#for g in gates:
#    print(f"{g} = {gates[g]}")

#for g in gates:
#    print(f"{g} = {res[g]}")

print(evg("a"))
