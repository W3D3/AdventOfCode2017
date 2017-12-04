file = open("day4/input.txt", "r")
input = file.read().splitlines()
sum = 0

def isAnagram(s1,s2):
    if len(s1) != len(s2):
        return False

    alist1 = list(s1)
    alist2 = list(s2)
    
    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print("AoC 2017 - Day 4 / Part 2")

for line in input:
    phrase = [ str(x) for x in line.split(' ') ]
    valid = True
    for i in range(0, len(phrase)):
        value1 = phrase[i]
        for j in range(0, len(phrase)):
            value2 = phrase[j]
            if i != j and isAnagram(value1, value2):
                # print(line + "=> INVALID cuz " + value1 + "//"+ value2)
                valid = False
                break
            pass
        if valid == False:
            break
    if valid:
        # print(line + "=> VALID")
        sum = sum + 1
    pass

print(sum)
