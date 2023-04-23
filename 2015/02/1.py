lines = open("input").readlines()

res = 0

for line in lines:
    l, w, h = map(int, line.split("x"))
    sides = [2 * l * w, 2 * w * h, 2 * h * l]
    print(sides)
    res += sum(sides) + min(sides) / 2

print(res)
