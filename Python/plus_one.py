def temp(arr, carry, ind):
    while carry > 0 and ind >= 0:
        # print("Carry: ", carry, "Ind: ", ind)
        if arr[ind] == 9:
            arr[ind] = 0
            ind -= 1
        
        else:
            arr[ind] += carry
            carry = 0
            break
    
    if ind == -1:
        # print(*arr)
        res = [1] + arr
        return res

    return arr


def solution(digits):
    l = len(digits) - 1
    
    if digits[l] == 9:
        digits[l] = 0
        # print(*digits)
        digits = temp(digits, 1, l - 1)
        return digits

    else:
        digits[l] += 1

    return digits

print(*solution([1,2,3]))
# arr = [5, 1, 2]
# arr.pop(0)
# print(*arr)