# aoc 15 3

visited = {(0, 0)}
current = (0, 0)

def move(c):
    global current, visited
    if c == '>':
        newHouse = (current[0]+1, current[1])
    elif c == '<':
        newHouse = (current[0]-1, current[1])
    elif c == '^':
        newHouse = (current[0], current[1]+1)
    elif c == 'v':
        newHouse = (current[0], current[1]-1)
    else:
        print("Error")
        exit()

    visited.add(newHouse)
    current = newHouse
   
        
with open("input.txt") as data:
    for line in data:
        for c in line:
            move(c)

print(len(visited))

        
