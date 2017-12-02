file = open("day1/input.txt", "r")
nums = list(file.read())
sum = 0

nums[len(nums)-1] = nums[0]; # let the array wrap

for i in range(0, len(nums) ):
    if i + 1 < len(nums):
        if nums[i] == nums[i + 1]:
            sum = sum + int(nums[i])
    pass

print(sum)
