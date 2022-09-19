'''Quick sort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.'''
'''Avearge time complexity is O(nlogn)'''
'''Worst case time complexity is O(n^2)'''
'''Space Complexity: O(1)'''
'''Worst case occurs when the array is already sorted'''
'''We can take pivot as any element in the array. We can also take median of the array as pivot.'''


def part(arr, left, right):
    '''Pivot is the last element of the array'''
    pvt = arr[right]
    itr = left

    '''Iterate through the array and swap the elements with the pivot'''
    for i in range(left, right):
        if(arr[i] < pvt):
            arr[itr], arr[i] = arr[i], arr[itr]
            itr += 1

    '''Swap the pivot with the element at the itr index'''
    arr[itr], arr[right] = arr[right], arr[itr]

    '''Return the index of the pivot'''
    return itr


def quickSort(arr, left, right):
    '''Base case'''
    if left < right:
        p = part(arr, left, right)
        quickSort(arr, left, p-1)
        quickSort(arr, p+1, right)

        
arr = [5, 2, 4, 6, 1, 3, 1, 0, -1, -8, 7]
quickSort(arr, 0, len(arr) - 1)
print(arr)