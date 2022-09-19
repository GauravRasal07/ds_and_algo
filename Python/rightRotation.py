def cyclicRotation(arr, val) :    #val : number of cyclic rotations
    size = len(arr)-1
    itr = 0
    while(itr < val) :
        temp = arr[size]
        for i in range(len(arr)) :
            arr[i], temp = temp, arr[i]
            
        itr += 1 
        
    return(arr)
    
print(cyclicRotation([1,2,3,4,5], 3))

def rotate(nums, k) -> None:
    length = len(nums)
    n = k % length
    def reverse_nodes(start, end):
        left, right = start, end
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            
            left += 1
            right -= 1
            
    reverse_nodes(0, length-1)
    reverse_nodes(0, n-1)
    reverse_nodes(n, length-1)