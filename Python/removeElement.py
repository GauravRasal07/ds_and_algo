# nums = [0,1,2,2,3,0,4,2]
# nums = [3,3,3]
nums = [3,2,2,3]
# nums = [1]

def solution(nums, val):
    print("Array: ", nums)
    first = 0
    last = len(nums) 
    if(len(nums) == 1 and nums[0] == val):
        return 0

    while(first < last):
        if nums[first] == val:
            nums[first] = nums[last - 1]
            last -= 1
        
        else:
            first += 1

    return last

k = solution(nums, 3)
# print("K: ", k)
print("array is:", nums[:k])