
f = open("data.txt", "r")

c = 0
p = 0
for x in f:
    if int(x) > p:
        c+=1
    p = int(x)

print(c-1)



