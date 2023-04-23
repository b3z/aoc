lines = open("input").readlines()

floor = 0
f = 1

for l in lines[0]:
    if l == "(":
        floor += 1
    elif l == ")":
        floor -= 1

    if floor < 0:
        break

    f += 1

print(f)
