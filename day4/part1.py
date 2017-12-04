file = open("day4/input.txt", "r")
input = file.read().splitlines()
sum = 0

print("AoC 2017 - Day 4 / Part 1")

for line in input:
    phrase = [ str(x) for x in line.split(' ') ]
    for value in phrase:
        valid = True
        if phrase.count(value) > 1:
            # print(line + "=> INVALID")
            valid = False
            break
        pass
    if valid:
        # print(line + "=> VALID")
        sum = sum + 1
    pass

print(sum)
