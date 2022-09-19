def solution(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if target < arr[mid]:
        return mid

    else:
        return mid + 1



if __name__ == '__main__':
    # nums = [1, 2, 4, 6, 7, 9, 10]
    nums = [1, 3]
    t = 0
    print(solution(nums, t))
    # print(bin_search(nums, t))
