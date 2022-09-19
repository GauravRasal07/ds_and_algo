nums = [4,2,4,0,0,3,0,5,1,0]

def solution(nums):
    slow = 0
    fast = 0

    while slow < len(nums):
        if nums[slow] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1

        slow += 1

    return nums

nums = solution(nums)
print(nums)