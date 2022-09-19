from traceback import print_tb


def solution(nums, k):
    l = len(nums)

    itr = 0

    # print(l, l-k)

    if k >= l and l > len(set(nums)):
        return True

    while itr <= (l - k):
        # print("Itr: ", itr)
        # print(nums[itr])
        # print(nums[itr+1: itr+k])
        if nums[itr] in nums[itr+1: itr+k+1]:
            print(nums[itr: itr+k])
            return True

        itr += 1

    itr -= 1
    # print(itr)
    # print(itr+k)
    # print(l)
    if(itr+k) <= l and len(nums[itr:]) != len(set(nums[itr:])):
        return True

    return False

print(solution(
[1,2,3,4,5,6,7,8,9,9]
, 3))
# print(solution([1,2,3,1], 3))
# print(solution([1,0,1,1], 1))
# print(solution([1,2,3,1,2,3], 2))