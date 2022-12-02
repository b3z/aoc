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

# x lose
# y draw
# z win

for s in l:
    e, m = s.split()
    if m == "X":  # lose
        if e == "A":
            total += 0 + moves["Z"]
        elif e == "B":
            total += 0 + moves["X"]
        elif e == "C":
            total += 0 + moves["Y"]
    if m == "Y":  # draw
        if e == "A":
            total += 3 + moves["X"]
        elif e == "B":
            total += 3 + moves["Y"]
        elif e == "C":
            total += 3 + moves["Z"]
    if m == "Z":  # win
        if e == "A":
            total += 6 + moves["Y"]
        elif e == "B":
            total += 6 + moves["Z"]
        elif e == "C":
            total += 6 + moves["X"]

print(total)
