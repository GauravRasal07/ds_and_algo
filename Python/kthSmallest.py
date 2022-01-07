def kthSmallest(arr, k):
    ar = arr
    for i in range(k-1) :
        ar.remove(min(ar))
        
    return(min(ar))
        
print(kthSmallest([7,10,4,3,20,15], 3))