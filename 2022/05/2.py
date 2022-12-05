moves = open("moves").readlines()

ca = [
    "RNPG",
    "TJBLCSVH",
    "TDBMNL",
    "RVPSB",
    "GCQSWMVH",
    "WQSCDBJ",
    "FQL",
    "WMHTDLFV",
    "LPBVMJF",
]

for c in range(len(ca)):
    ca[c] = [char for char in ca[c]]

tmp = []

for m in moves:
    qua = int(m.split(" ")[1])
    fro = int(m.split(" ")[3])
    to = int(m.split(" ")[5])

    for q in range(qua):
        tmp.append(ca[fro - 1].pop(-1))

    tmp.reverse()
    ca[to - 1] = ca[to - 1] + tmp
    tmp = []

s = ""
for c in ca:
    s += c[-1]

print(s)
