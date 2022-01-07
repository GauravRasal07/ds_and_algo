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