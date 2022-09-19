def isPalindrome(x):
    numString = str(x)

    return numString == numString[::-1]


print(isPalindrome(121))
print(isPalindrome(-1221))