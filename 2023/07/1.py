from collections import Counter


# smart idea from stackoverflow
def get_rank(cs, bid):
    # Nums 2-9, then 10-14 are pictures
    cs = cs.replace("T", chr(ord("9") + 1))
    cs = cs.replace("J", chr(ord("9") + 2))
    cs = cs.replace("Q", chr(ord("9") + 3))
    cs = cs.replace("K", chr(ord("9") + 4))
    cs = cs.replace("A", chr(ord("9") + 5))

    ocs = Counter(cs)
    val = sorted(ocs.values())

    if val == [5]:  # five of a kind
        return (10, cs, bid)
    elif val == [1, 4]:  # four of kind
        return (9, cs, bid)
    elif val == [2, 3]:  # full house
        return (8, cs, bid)
    elif val == [1, 1, 3]:  # three of a kind
        return (7, cs, bid)
    elif val == [1, 2, 2]:  # two pairs
        return (6, cs, bid)
    elif val == [1, 1, 1, 2]:  # one pair
        return (5, cs, bid)
    elif val == [1, 1, 1, 1, 1]:  # high card
        return (4, cs, bid)
    else:
        print("Error")
        exit()


rank = []
for l in open(0):
    cs, bid = l.split()
    rank.append(get_rank(cs, bid))

res = 0
for i, r in enumerate(sorted(rank)):
    res += (i + 1) * int(r[2])
print(res)
