f = open(0).read().splitlines()

sum = 0
for l in f:
    win, my = l.split(': ')[1].split(' | ')
    t = 0
    win = win.split(' ')
    my = my.split(' ')
    for w in win:
        if w == '':
            win.remove(w)
    for m in my:
        if m == '':
            my.remove(m)

    for m in my:
        if m in win:
            if t == 0:
                t = 1
            else:
                t= 2*t

    sum += t
    t = 0

print(sum)

