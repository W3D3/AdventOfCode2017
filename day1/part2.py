def matchingIndex(i, length):
    return int((i + length / 2) % length)

file = open("day1/input.txt", "r")
nums = list(file.read())
sum = 0
nums.pop() # remove linebreak

for i in range(0, len(nums) ):
    if nums[i] == nums[matchingIndex(i, len(nums))]:
        sum = sum + int(nums[i])
    pass
print(sum)
