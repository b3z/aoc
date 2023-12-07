from collections import Counter
import copy


def get_rank(cs, bid):
    cso = cs
    cs = cs.replace("J", chr(ord("2") - 1))  # joker. Make smaller than 2
    cs = cs.replace("T", chr(ord("9") + 1))
    cs = cs.replace("Q", chr(ord("9") + 3))
    cs = cs.replace("K", chr(ord("9") + 4))
    cs = cs.replace("A", chr(ord("9") + 5))

    ocs = Counter(cs)
    new_ocs = copy.deepcopy(ocs)

    for c in ocs.keys():  # find biggest in hand and add to this.
        if c == chr(ord("2") - 1):
            if new_ocs.get(c) == 5:  # case 5 J
                new_ocs["2"] = new_ocs.get(c)
                del new_ocs["1"]
                continue

            del new_ocs["1"]
            sr = sorted(new_ocs.items(), key=lambda x: x[1])[::-1]
            new_ocs[sr[0][0]] += ocs.get(c)

    val = sorted(new_ocs.values())

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
        print(val)
        exit()


rank = []
for l in open(0):
    cs, bid = l.split()
    rank.append(get_rank(cs, bid))

res = 0
for i, r in enumerate(sorted(rank)):
    res += (i + 1) * int(r[2])
print(res)
