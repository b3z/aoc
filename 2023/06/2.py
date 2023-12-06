time, *dist = open(0).read().splitlines()

t = int(time.split(':')[1].replace(' ', ''))
d = int(dist[0].split(':')[1].replace(' ', ''))

res = 1
possible=0
for hold in range (t):
    run = t - hold
    if run*hold > d:
        possible+=1
res *= possible
print(res)
