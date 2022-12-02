f = open("input")
l = f.readlines()

moves = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

total = 0

for s in l:
    m = s.split()[1]
    c = s.replace(" ", "").replace("\n", "")

    if c in ["AX", "BY", "CZ"]:  # draw
        total += 3
    elif c in ["AY", "BZ", "CX"]:  # win
        total += 6
    elif c in ["AZ", "BX", "CY"]:  # loss
        total += 0
    total += moves[m]

print(total)
