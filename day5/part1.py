file = open("day5/input.txt", "r")
input = file.read().splitlines()
count = 0
i = 0

print("AoC 2017 - Day 5 / Part 1")

while i >= 0 and i < len(input):
    current = int(input[i])
    # print(current)
    input[i] = current + 1;
    i = i + current;
    count = count + 1

print(count)
