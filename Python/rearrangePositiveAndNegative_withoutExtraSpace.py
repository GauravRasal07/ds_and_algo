'''
Rearrange positive and negative numbers without using extra space
'''

Input =  [12, 11, -13, -5, 6, -7, 5, -3, -6]
# Input =  [-1, 2, -3, 4, 5, 6, -7, 8, 9]
Output = [-13, -5, -7, -3, -6, 12, 11, 6, 5]
# Output = [-1, -3, -7, 2, 4, 5, 6, 8, 9]

p1 = 0
p2 = len(Input)-1
while(p1 < p2):
    if(Input[p1] < 0 and Input[p2] < 0):
        p1+=1

    elif(Input[p1] > 0 and Input[p2] > 0):
        p2-=1

    elif(Input[p1] < 0 and Input[p2] > 0):
        p1+=1
        p2-=1

    else:
        Input[p1], Input[p2] = Input[p2], Input[p1]
        p1+=1
        p2-=1

print(Input)


'''Function to right rotate the array'''
def rotate(arr,l,h):
    last=arr[h]
    for i in range(h,l,-1):
        arr[i]=arr[i-1]
    arr[l]=last
    return arr

def negativeFirst(Input):
    j = 0
    for i in Input:
        if(i < 0):
            temp = i
            Input = rotate(Input, j, Input.index(i))
            j+=1

print(negativeFirst(Input))

# if(Input == Output):
#     print("Pass")

# else:
#     print("Fail")
            