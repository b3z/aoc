f = open("data.txt", "r")
h=0
d=0

def parse(s):
    global h, d
    c = s.split(' ')[0]
    v = int(s.split(' ')[1])
    if c == "forward":
        h+=v
    if c == "down":
        d+=v
    if c=="up":
        d-=v



for x in f:
    parse(x)

print(h*d)
