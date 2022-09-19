def decryptPassword(s) :
    '''
    Given a string of numbers and special characters, return the decrypted password
    
    :param s: the encrypted password
    :return: The decrypted password.
    '''
    nums = ["1", "2" ,"3", "4", "5", "6", "7", "8", "9"]
    res = []
    stack = []
    for i in range(0, len(s)) :
        if(s[i] in nums) :
            stack.append(s[i])
            
        elif(s[i] == "0") :
            temp = stack[len(stack)-1]
            res.append(temp)
            stack.pop(len(stack)-1)
            
        elif(s[i] == "*") :
            l = len(res)
            res[l-1], res[l-2] = res[l-2], res[l-1]
            
        else :
            res.append(s[i])
            
    return ("".join(res))
    
print(decryptPassword("51Pa*0Lp*0e"))
print(decryptPassword("43Ah*ck0rr0nk"))