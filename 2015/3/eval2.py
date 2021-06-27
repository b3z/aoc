# aoc 15 3

visited = {(0, 0)}
currentSanta = (0, 0)
currentRobot = (0, 0)
robotTurn = False

def move(c):
    global visited, robotTurn, currentSanta, currentRobot

    if robotTurn:
        current = currentRobot
        robotTurn = False
    else:
        current = currentSanta
        robotTurn = True

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

    current = 0

    visited.add(newHouse)

    if not robotTurn: # invert due to robotTurn switch in the upper statement
        currentRobot = newHouse
    else:
        currentSanta = newHouse
        
with open("input.txt") as data:
    for line in data:
        for c in line:
            move(c)

print(len(visited))

        
