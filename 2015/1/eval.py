# aoc 2015 1

input = "input.txt"
result = 0

idx = 0
firstBasementIdx = -1

with open(input) as inst:
    for line in inst:
        for c in line:
            idx += 1
            if c == '(': # up one floor
                result += 1
            else:
                result -= 1 # down one floor (case ')')

            if firstBasementIdx == -1: # did we find a first basement yet? true == no.
                if result == -1: # first basement.
                    firstBasementIdx = idx # set index of first basement.

print(result)
print(f'First basement index: {firstBasementIdx}')
                
