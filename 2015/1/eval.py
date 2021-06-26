# aoc 2015 1

input = "input.txt"
result = 0

with open(input) as inst:
    for line in inst:
        for c in line:
            if c == '(': # up one floor
                result += 1
            else:
                result -= 1 # down one floor (case ')')

print(result)
                
