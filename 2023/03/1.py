fs = open(0).read().splitlines()

num = ''
sum = 0

for y, row in enumerate(fs):
    for x, c in enumerate(row):
        if c.isdigit():
            num += c
        if (not c.isdigit() or x >= len(fs[0])-1) and num != '':
            if x > len(fs[0]):
                x+=1
            x1 = max((x-len(num)-1), 0)
            x2 = min((x+1), len(fs[0])-1)
            y1 = max(y-1, 0)
            y2 = min(y+1, len(fs)-1)
            s = [t[x1:x2] for t in fs[y1:y2+1]]
            print(s)
            for t in s:
                if any(not t1.isdigit() and t1 != '.' for t1 in t):
                    sum += int(num)
                    break

            num = ''
        continue

print(sum)
