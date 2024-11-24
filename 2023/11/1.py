G = open(0).read().splitlines()

row_empty = [i for i, row in enumerate(G) if all(c == '.' for c in row)]
col_empty = [i for i, col in enumerate(zip(*G)) if all(c == '.' for c in col)]

points = [(r, c) for r, row in enumerate(r, row)

