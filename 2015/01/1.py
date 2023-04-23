lines = open("input").readlines()

floor = 0

for l in lines[0]:
    if l == '(':
        floor += 1
    elif l == ')':
        floor -= 1

print(floor)
