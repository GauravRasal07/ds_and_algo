'''Arrange given numbers to form the biggest number'''
'''Unsolved'''

'''def largestNumber(array):
      
    # extval is a empty list for extended 
    # values and ans for calculating answer
    extval, ans = [], ""
      
    # calculating the length of largest number
    # from given and add 1 for further operation
    l = len(str(max(array))) + 1
      
    # iterate given values and 
    # calculating extended values
    for i in array:
        temp = str(i) * l
          
        # make tuple of extended value and 
        # equivalant original value then 
        # append to list
        extval.append((temp[:l:], i))
      
    # sort extval in descending order
    extval.sort(reverse = True)
      
    # iterate extended values
    for i in extval:
          
        # concatinate original value equivalant
        # to extended value into ans variable
        ans += str(i[1])
  
    if int(ans)==0:
        return "0"
    return ans
  
# Driver code
a = [1, 34, 3, 98, 9, 76,
        45, 4, 12, 121]
  
print(largestNumber(a))'''



import collections

# inp = [54, 546, 548, 60]
inp = [1, 34, 3, 98, 9, 76, 45, 4]
# out = '6054854654'
out = '998764543431'

temp = {}
for i in inp:
    if(i % 10 == 0):
        temp.update({(i%10):inp.index(i)})
    else:
        temp.update({(10 - (i%10)):inp.index(i)})

res = []
# temp = 
for i in collections.OrderedDict(sorted(temp.items())):
    # res.append(inp[temp[i]])
    res.append(inp[temp[i]])

print(''.join(map(str, res)))