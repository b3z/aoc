
vowels = list("aeiou") # at least 3
forbidden = ["ab", "cd", "pq", "xy"] # none
# at least one letter twice in a row

# takes string, returns true if string is naughty
def isNaughty(s):
    if any(f in s for f in forbidden):
        return True
    
    numVowels = 0
    letterTwice = False
    letterTmp = ''

    for c in s:
        if c in vowels:
            numVowels += 1

        if c == letterTmp:
            letterTwice = True
        else:
            letterTmp = c
    
    if numVowels >= 3 and letterTwice:
        return False

    return True


assert isNaughty("ugknbfddgicrmopn") == False, "Should be a nice String"
assert isNaughty("aaa") == False, "Should be a nice String"
assert isNaughty("jchzalrnumimnmhp") == True, "Should be naughty"
assert isNaughty("haegwjzuvuyypxyu") == True, "Should be naughty"
assert isNaughty("dvszwmarrgswjxmb") == True, "Should be naughty"
print("All tests passed.")

numNiceStrings = 0

with open("input.txt") as data:
    for line in data:
        if not isNaughty(line):
            numNiceStrings += 1

print(f'Number of nice strings: {numNiceStrings}')

