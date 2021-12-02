f = open("data.txt", "r")
h=0
d=0
aim=0

def parse(s):
    global h, d, aim
    c = s.split(' ')[0]
    v = int(s.split(' ')[1])
    if c == "forward":
        h+=v
        d+=(aim*v)
    if c == "down":
        aim+=v
    if c=="up":
        aim-=v



for x in f:
    parse(x)

print(h*d)
