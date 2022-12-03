f = open("input")
lines = f.readlines()

sum = 0
for l in lines:
    a = [l[i : i + int(len(l) / 2)] for i in range(0, len(l), int(len(l) / 2))]
    for s in a[0]:
        if s in a[1]:
            print(s)
            pos = ord(s.lower()) - 96
            if s.isupper():
                pos += 26
            sum += pos
            print(pos)
            break
print(sum)
