f = open(0).read().splitlines()
import re

sc = [1]*len(f)

sum = 0
for l in f:
    id = l.split(': ')[0]
    id = re.findall(r"\d+$", id)[0]
    id = int(id)
    win, my = l.split(': ')[1].split(' | ')
    t = 0
    win = win.split(' ')
    my = my.split(' ')

    # this is stupid shit because I parse bad.
    for w in win:
        if w == '':
            win.remove(w)
    for m in my:
        if m == '':
            my.remove(m)
    for m in my:
        if m in win:
            t += 1

    for i in range(id+1, id+t+1):
        if i < len(f)+1:
            sc[i-1] += sc[id-1]
    t = 0

for s in sc:
    sum += s

print(sum)
