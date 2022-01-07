def reverseArray(arr) :
    start = 0
    end = len(arr)-1
    itr = int(len(arr)//2)    #Array is sorted in size of the array by 2 iterations.
    for i in range(itr) :
        arr[start], arr[end] = arr[end], arr[start]
        start = start+1
        end = end-1
    
    print(arr)
        
reverseArray([1, 2, 3, 4 ,5, 6, 7, 8])