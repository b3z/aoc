from collections import deque

file = open('input')
grid = [list(x) for x in file.read().strip().splitlines()]

for r, a in enumerate(grid):
    for c, b in enumerate(a):
        if b == 'S':
            sp = (r, c)
            grid[r][c] = 'a'
        if b == 'E':
            ep = (r, c)
            grid[r][c] = 'z'

q = deque()
q.append((0, ep[0], ep[1]))

vis = {ep}

while q:  # as long q not empty
    d, r, c = q.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue

        if (nr, nc) in vis:
            continue

        # print(nr, nc)
        if ord(grid[nr][nc]) - ord(grid[r][c]) < -1:
            continue

        if grid[nr][nc] == 'a':
            print(d + 1)
            exit(0)

        vis.add((nr, nc))
        q.append((d + 1, nr, nc))
