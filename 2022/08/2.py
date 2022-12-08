lines = open("input").readlines()

grid = [list(map(int, l.strip())) for l in lines]

hs = 0
z = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        current = grid[r][c]
        score = 1

        for x in range(c + 1, len(grid[r])):
            z += 1
            if grid[r][x] >= current:
                break

        score *= z
        z = 0

        for x in range(c - 1, -1, -1):
            z += 1
            if grid[r][x] >= current:
                break

        score *= z
        z = 0

        for x in range(r + 1, len(grid)):
            z += 1
            if grid[x][c] >= current:
                break

        score *= z
        z = 0

        for x in range(r - 1, -1, -1):
            z += 1
            if grid[x][c] >= current:
                break

        score *= z
        z = 0

        hs = max(hs, score)

print(hs)
