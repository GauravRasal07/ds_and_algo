def intersectionAndUnion(arr1, arr2) :
    # union = []
    # intersection = []
    # for i in arr1 :
    #     if i in arr2 and i not in intersection:
    #         intersection.append(i)
            
    #     union.append(i)
        
    # for j in arr2 :
    #     if j not in union :
    #         union.append(j)
            
    return(list(set(arr1) | set(arr2)), list(set(arr1) & set(arr2)))
    
print(intersectionAndUnion([0,1,2,3,4,5], [4,5,6,7,8,9]))