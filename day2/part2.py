file = open("day2/input.txt", "r")
input = file.read().splitlines()
sum = 0

print("AoC 2017 - Day 2 / Part 2")

for line in input:
    # print(line)
    row = [ int(x) for x in line.split('\t') ]
    for i in range(0, len(row) ):
        for j in range(0, len(row)):
            if i != j: #if not the same number
                if row[i] % row[j] == 0:
                    # print(str(row[i]) + " is devidable by " + str(row[j]))
                    result = row[i] / row[j]
                    sum = sum + result
                    # print(result)
    pass

print(sum)
