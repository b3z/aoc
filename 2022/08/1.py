lines = open('input').readlines()

grid = [list(map(int, l.strip())) for l in lines]

vis = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        current = grid[r][c]
        if all(grid[r][i] < current for i in range(c)):
               vis += 1
        elif all(grid[r][i] < current for i in range(c+1, len(grid[r]))):
               vis += 1
        elif all(grid[i][c] < current for i in range(r)):
               vis += 1
        elif all(grid[i][c] < current for i in range(r+1, len(grid[c]))):
               vis += 1

print(vis)
