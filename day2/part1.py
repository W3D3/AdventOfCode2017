file = open("day2/input.txt", "r")
input = file.read().splitlines()
sum = 0

print("AoC 2017 - Day 2 / Part 1")

for line in input:
    row = [ int(x) for x in line.split('\t') ]
    checksum = max(row) - min(row)
    sum = sum + checksum;
    pass

print(sum)
