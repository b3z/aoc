
class Grid:
    def __init__(self):
        self.grid = [[0 for x in range(1000)] for y in range(1000)]  # 1000 x 1000 grid

    def apply(self, c1, c2, value):
        while c1[0] <= c2[0]:
            tmp = c1[1]
            while tmp <= c2[1]:
                state = self.grid[c1[0]][tmp]
                self.grid[c1[0]][tmp] = self.grid[c1[0]][tmp] + value
                if self.grid[c1[0]][tmp] < 0:
                    self.grid[c1[0]][tmp] = 0
                tmp += 1
            c1[0] += 1

    # +1
    def on(self, c1, c2):
        self.apply(c1, c2, 1)

    # -1
    def off(self, c1, c2):
        self.apply(c1, c2, -1)

    # +2
    def toggle(self, c1, c2):
        self.apply(c1, c2, 2)

    def print(self):
        for row in self.grid:
            print(row)

    def countOn(self):
        numOn = 0
        for row in self.grid:
            numOn += sum(row)
        return numOn

g = Grid()

with open("input.txt") as data:
    for line in data:
        inst = line.split(' ')
        
        c1 = list(map(int, inst[-3].split(',')))
        c2 = list(map(int, inst[-1].split(',')))

        if inst[0] == "toggle":
            g.toggle(c1, c2)
        elif inst[1] == "on":
            g.on(c1, c2)
        else:
            g.off(c1, c2)

print(f'Lights on: {g.countOn()}')
