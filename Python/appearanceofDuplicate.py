from collections import Counter

def firstRepeated(arr, n):
        
        #arr : given array
        #n : size of the array
        temp = Counter(arr)

        res = -1
        
        for i in temp:
            if temp[i] > 1:
                res = arr.index(i) + 1
                break

        return res

# print(firstRepeated([1, 5, 3, 4, 3, 5, 6], 7))

def firstNonRepeating(arr, n): 
        # Complete the function
        temp = Counter(arr)
        
        for i in temp:
            if(temp[i] == 1):
                return i
                
        return 0

print(firstNonRepeating([-1, -17, -12, 8, 16, -17, -13, -14, -3, -6, -5, -11, -10, -12, -5, 19, -17, -5, -1, 12], 20))