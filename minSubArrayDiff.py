# def getMinDiff(arr, k):
#         # code here
#         mini = min(arr) + k
#         maxi = max(arr) - k
#         for i in arr :
#             if(i < k) :
#                 temp2 = i + k
#                 if(temp2 > maxi and temp2 < max(arr)) :
#                     maxi = temp2
                
#             elif(i > k) :
#                 temp1 = i - k
#                 if(temp1 < mini and temp1 >= 0) :
#                     mini = temp1

#         print(maxi - mini)
        
# getMinDiff([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 5)

def minDiff(arr, k) :
    new_arr = []
    for i in arr :
        if(i == max(arr)) :
            new_arr.append(i - k)
            
        else :
            new_arr.append(i + k)
            
    a = max(new_arr) - min(new_arr)
    
    mini = min(arr) + k
    maxi = max(arr) - k
    for i in arr :
        if(i <= k) :
            temp2 = i + k
            if(temp2 > maxi and temp2 < max(arr)) :
                maxi = temp2
            
        elif(i == max()) :
            temp1 = i - k
            if(temp1 < mini and temp1 >= 0) :
                mini = temp1

    b = (maxi - mini)
    if(a < b):
        return a
        
    else :
        return b
    
print(minDiff([5, 5, 8, 6, 4, 10, 3, 8, 9, 10], 5))