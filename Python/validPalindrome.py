def isPalindrome(s):
    return s == s[::-1]

s = "z A man, a plan, a canal: Panama"
# s= "8,9"
res = ""

for i in s:
    i = i.lower()
    # print(i, end=" ")
    # print("Res: ",res)
    if ord(i) in range(97, 122) or ord(i) in range(48, 57):
        res += i

print(res)
print(isPalindrome(res))