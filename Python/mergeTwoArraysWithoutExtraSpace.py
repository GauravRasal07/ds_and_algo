def merge(arr1, arr2, n, m): 
        '''More Time Complexity'''
        # loop = min(m, n)
        # itr = 0
        # while(itr < n):
        #     if(arr1[itr] >= arr2[0]):
        #         arr1[itr], arr2[0] = arr2[0], arr1[itr]
        #         itr += 1
                
        #         arr2.sort()
                    
        #     else:
        #         itr += 1


        '''Optimized Time Complexity'''
        a = n-1
        b = 0
        while(b<m):
            if(arr1[a] > arr2[b]):
                arr1[a], arr2[b] = arr2[b], arr1[a]
                a -= 1
                b += 1
            else:
                b += 1

        arr1.sort()
        arr2.sort()
 

arr_1 = '2 6 7 8 9 9 10 10 11 12 12 12 12 13 13 13 14 15 16 16 17 18 18 19 20'.split()
arr_2 = '1 5 5 7 7 8 9 11 15 18 18 18 20 20'.split()
arr1, arr2 = [], []
for i in arr_1:
    arr1.append(int(i))
for i in arr_2:
    arr2.append(int(i))

merge(arr1, arr2, len(arr1), len(arr2) )
print(arr1)
print(arr2)

