'''Rearrange an array such that ‘arr[j]’ becomes ‘i’ if ‘arr[i]’ is ‘j’ '''

inp = [2, 0, 1, 4, 5, 3];
out = [1, 2, 0, 5, 3, 4];

temp_arr = [0]*len(inp)
for i in range(len(inp)):
    temp = inp[i]
    temp_arr[temp] = i
print(temp_arr)
