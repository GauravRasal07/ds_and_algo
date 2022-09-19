a1 = [2,1,0,0]
a2 = [3,2,1,0,4]
a3 = [3,0,8,2,0,0,1]
a4 = [5,9,3,2,1,0,2,3,3,1,0,0]

def canJump(nums):
    l = len(nums)
    ans = True
    i = 0
    if l == 1:
        return True
    while i < l:
        ele = nums[i]
        if i > (l-1) or i + ele >= (l-1):
            print("Returning True")
            return True

        if ele == 0:
            ans = False
            return ans

        # print(nums[(i+1):(i+ele+1)])
        next = max(nums[(i+1):(i+ele+1)])
        if next > len(nums[i:]) or i + ele >= (l-1):
            return ans

        for j in range(i+1, i+ele+1):
            if nums[j] == next:
                i += j

    return ans


print(canJump(a1))
# print(canJump(a2))
# print(canJump(a3))
# print(canJump(a4))