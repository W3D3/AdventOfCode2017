file = open("day6/input.txt", "r")
input = file.read().splitlines()
bank = [ int(x) for x in input[0].split('\t') ]
seen = []
found = False
count = 0
loops = 0

def getMaxIndex(arr):
    max = 0
    for i in range(0, len(arr)):
        if arr[i] > arr[max]:
            max = i
        pass
    return max

print("AoC 2017 - Day 6 / Part 1")

while found == False:
    count = count + 1
    i = getMaxIndex(bank);
    toDistrubute = bank[i]
    bank[i] = 0

    for x in range(0, toDistrubute):
        i = (i + 1) % len(bank)
        bank[i] = bank[i] + 1
        pass

    if str(bank) in seen:
        found = True
        indices = [i for i, el in enumerate(seen) if el == str(bank)]
        print(len(seen) - indices[0])

    seen.append(str(bank))
