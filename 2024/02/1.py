f = open('input')

safe = 0

def check(r):
    r = list(map(int, r.split(' ')))
    a = sorted(r)
    d = a[::-1]
    if a == r or d == r:
        p = r[0]
        for c in r[1:len(r)]:
            diff = abs(p-c)
            if diff > 3 or diff < 1:
                return False
            p = c
        return True
    else:
        return False

for r in f:
    if check(r):
        safe +=1

print(safe)


