'''Merge Sort Algorithm uses divide and conquer approach to sort an array.'''
'''Time Complexity: O(n log n)'''
'''Space Complexity: O(n)'''


'''Conqueor function is used to merge the two subarrays'''
def conqueor(arr, start, mid, end):
    merged = []
    ind1 = start
    ind2 = mid + 1

    '''Merge the two subarrays'''
    while ind1 <= mid and ind2 <= end:
        if arr[ind1] < arr[ind2]:
            merged.append(arr[ind1])
            ind1 += 1
        else:
            merged.append(arr[ind2])
            ind2 += 1

    '''If there are elements left in the first half'''
    while ind1 <= mid:
        merged.append(arr[ind1])
        ind1 += 1
    
    '''If there are elements left in the second half'''
    while ind2 <= end:
        merged.append(arr[ind2])
        ind2 += 1

    '''From two of the above loops only one loop will be executed'''

    '''Copy the merged array to the original array'''
    for i in range(len(merged)):
        arr[start + i] = merged[i]


'''Divide the array into two halves'''
def divide(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        divide(arr, start, mid)
        divide(arr, mid + 1, end)
        conqueor(arr, start, mid, end)
        

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = [5, 2, 4, 6, 1, 3, 1, 0, -1, -8, 7]
divide(arr, 0, len(arr)-1)
print(arr)    