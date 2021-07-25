
ops = {
    "NOT"       : lambda x, y : ~x, # takes two args, only the first is evaluated
    "AND"       : lambda x, y : x & y,
    "OR"        : lambda x, y : x | y,
    "RSHIFT"    : lambda x, y : x >> y,
    "LSHIFT"    : lambda x, y : x << y
    }

class Int:
    def __init__(self):
        self.val = -1 
    
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
            print(f.get())
        else:
            f = getRef(t[0])
    elif lt == 2:
        if t[1].isdecimal():
            f = [t[0], Int().set(t[1]), Int()]
        else:
            f = [t[0], getRef(t[1]), Int()]
    else:
        if t[0].isdecimal() is not True:
            t[0] = getRef(t[0])
        else:
            tmp = Int()
            tmp.set(t[0])
            t[0] = tmp

        if t[2].isdecimal() is not True:
            t[2] = getRef(t[2])
        else:
            tmp = Int()
            tmp.set(t[2])
            t[2] = tmp

        f =  [t[1], t[0], t[2]]
        print(f"{target} = {f}")
    
    gates[target] = f

def getRef(x):
    global gates
    try:
        f = gates[x].get()
    except:
        gates[x] = Int().set(-1)
    finally:
        f = gates[x]
    return f

gates = {}

def evg(g):
    if type(g) == Int:
        return g.get()

    return ops[g[0]](g[1].get(), g[2].get()) & ((1<<16)-1)

with open("input.debug") as data:
    for line in data:
       #gates[line.split(" -> ")[1]] = Gate(line)
       make(line)


for gate in gates:
    g = gates[gate]
    try:
        print(f"{gate} = {g[0]} {g[1]} {g[2]}")
        print(f"{gate} = {g[0]} {type(g[1])} {type(g[2])}")
    except:
        print(gate)

    
print("\nEval")
for g in gates:
    print(f"{g}: {evg(gates[g])}")
