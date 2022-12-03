f = open("input")
lines = f.readlines()

sum = 0
for i in range(0, len(lines), 3):
    for c in lines[i]:
        if c in lines[i + 1] and c in lines[i + 2]:
            print(c)
            pos = ord(c.lower()) - 96
            if c.isupper():
                pos += 26
            sum += pos
            break
print(sum)
