def matchingIndex(i, length):
    return int((i + length / 2) % length)

file = open("./input.txt", "r")
nums = list(file.read())
sum = 0
nums.pop() # remove linebreak

nums[len(nums)-1] = nums[0]; # let the array wrap
print(len(nums))
for i in range(0, len(nums) ):
    print("nums["+str(i)+"] >> "+nums[i])
    if nums[i] == nums[matchingIndex(i, len(nums))]:
        print(nums[i])
        sum = sum + int(nums[i])
    pass

print(sum)
