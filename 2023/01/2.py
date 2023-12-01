file = open('input')

sum = 0
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for f in file:
    w = []
    for d, c in enumerate(f):
        if c.isdigit():
            w.append(c)
        for i, n in enumerate(nums):
            if f[d:].startswith(n):
                w.append(str(i + 1))

    sum += int(w[0] + w[-1])

print(sum)
