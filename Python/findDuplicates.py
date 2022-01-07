# Solution-1

def findDuplicate(nums):
        temp = []
        for i in nums :
            if i in temp :
                return i
            
            temp.append(i)

print(findDuplicate([1, 3, 4, 2, 2]))

# Solution-2

def findDuplicate(nums):
        for i in nums:
            temp = nums.index(i)
            temp += 1
            if i in nums[temp:] :
                return i

print(findDuplicate([1, 3, 4, 2, 2]))

# Solution from Discussion

def findDuplicate(nums) :
        for index in range(len(nums)):
            cur = abs(nums[index])
            print(cur)
            print(nums[cur])
            if nums[cur] < 0:
                return cur
            nums[cur] *= - 1
            print(nums)
            
print(findDuplicate([1, 3, 4, 2, 2]))  