class M:
    def __init__(self, id, items, op, test, testActions):
        self.id = id
        self.items = items
        self.op = op
        self.test = test
        self.testActions = testActions
        self.count = 0

    def inspect(self, item):
        self.count = self.count + 1
        item = self.op(item)
        item %= common_mod
        self.items.pop(0)
        if item % self.test == 0:
            self.throwTo(self.testActions[0], item)
        else:
            self.throwTo(self.testActions[1], item)


    def throwTo(self, id, item):
        global monkey
        monkey[id].items.append(item)

    def takeTurn(self):
        itemsC = list(self.items)
        for item in itemsC:
            self.inspect(item)

    def __str__(self):
        return str(self.items)

monkey = [
        M(0, [93, 98], lambda x : x * 17, 19, [5, 3]),
        M(1, [95, 72, 98, 82, 86], lambda x : x + 5, 13, [7, 6]),
        M(2, [85, 62, 82, 86, 70, 65, 83, 76], lambda x : x + 8, 5, [3, 0]),
        M(3, [86, 70, 71, 56], lambda x : x + 1, 7, [4, 5]),
        M(4, [77, 71, 86, 52, 81, 67], lambda x : x + 4, 17, [1, 6]),
        M(5, [89, 87, 60, 78, 54, 77, 98], lambda x : x * 7, 2, [1, 4]),
        M(6, [69, 65, 63], lambda x : x + 6, 3, [7, 2]),
        M(7, [89], lambda x : x * x, 11, [0, 2])
]

common_mod = 1
for m in monkey:
    common_mod *= m.test

for n in range(10000):
    for m in monkey:
        m.takeTurn()

c = []
for m in monkey:
    c.append(m.count)

c = sorted(c)
print(c[-1]*c[-2])
