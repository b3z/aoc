inp = "1113222113"

def run(s):
    c = 0
    a = None
    res = []
    for i in range(len(s)):
        if a == None:
            a = s[i]
            c += 1
            continue

        if s[i] == a:
            c += 1

        else:
            res.append(str(c) + a)
            a = s[i]
            c = 1

    res.append(str(c) + a)

    return ''.join(res)

for s in range(40):
    inp = run(inp)

print(len(inp))
