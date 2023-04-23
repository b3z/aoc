lines = open("input").read().splitlines()

moves = {"L": -1, "R": 1, "U": 1j, "D": -1j}

kts = [0 for _ in range(10)]
vis = set()

for line in lines:
    move, steps = line.split()
    kts[0] += int(steps) * moves[move]

    while True:
        for i in range(1, len(kts)):
            diff = kts[i - 1] - kts[i]

            if abs(diff) < 2:
                break

            kts[i] += complex(
                diff.real // abs(diff.real) if diff.real else 0,
                diff.imag // abs(diff.imag) if diff.imag else 0,
            )

        else:
            vis.add(kts[-1])
            continue
        break

print(len(vis))
