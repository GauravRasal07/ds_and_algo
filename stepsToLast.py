def stepsToLast(n, arr):
    res = 0
    cnt = 0
    for i in arr:
        cnt += 1
        res = res + i
        if (res >= n-1):
            break

    return cnt

print(stepsToLast(11, [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
    