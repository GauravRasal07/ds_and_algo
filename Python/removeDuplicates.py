nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

k = removeDuplicates(nums)

for i in range(k):
    print(nums[i], end=' ')