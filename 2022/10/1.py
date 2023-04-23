lines = open("input").read().splitlines()
r = [n for n in range(20, 221, 40)]

clk = 0
x = 1
sum = 0

def solve(cmd):
    global clk, x, sum
    clk += 1

    if clk in r:
        sig = x * clk
        sum += sig

    if cmd == "noop":
        return
    else:
        n = int(cmd.split()[1])
        solve("noop")
        x += n

while 1:
    if len(lines) == 0:
        break

    cmd = lines.pop(0)
    solve(cmd)

print(sum)
