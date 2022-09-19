# arr = [10,20,5,8,6,7,9,3,4,2,1]
arr = [8,2,1,1,7,5,3,2,4,3,9,3]

def divideArray(arr, k):
    if not arr or k <= 0:
        print("Invalid input")
        return None

    s = sum(arr)
    print("Sum: ", s)
    print("Length: ", len(arr))

    if s % k != 0:
        print("The given array can't be divided into k parts having equal sum")
        return None

    s = s // k

    arr.sort()

    arr = arr[::-1]

    # print("Sorted array: ", arr)

    for i in range(len(arr)):
        temp = arr[i]
        if temp == 0:
            continue

        if k == 0:
            break
        rem = s - temp
        print("i: ", temp, "rem: ", rem)
        if rem == 0:
            k -= 1
            print(temp)

        elif rem > 0:
            print(temp)
            for j in range(i+1, len(arr)):
                # print("J: ", j, "arr[j]: ", arr[j])
                if arr[j] == 0:
                    continue

                if arr[j]<= rem:
                    print(arr[j])
                    rem -= arr[j]
                    arr[j] = 0

                if rem == 0:
                    k -= 1
                    print(arr[j], end=" ")
                    break
        print() 




    
divideArray(arr, 4)