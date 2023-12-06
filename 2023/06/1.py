time, *dist = open(0).read().splitlines()

time = list(map(int, time.split(':')[1].split()))
dist = list(map(int, dist[0].split(':')[1].split()))

res = 1
for t, d in zip(time, dist):
    possible=0
    for hold in range (t):
        run = t - hold
        if run*hold > d:
            possible+=1
    res *= possible
print(res)

