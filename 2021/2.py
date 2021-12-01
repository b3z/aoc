f = open("data.txt", "r")

c = 0
f = list(map(int, f))

for i in range(len(f)-3):
    if f[i] < f[i+3]:
        c+=1

print(c)



