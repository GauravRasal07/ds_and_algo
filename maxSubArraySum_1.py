def maxSubArraySum(a,size): 
           
        max_so_far = -9999999 - 1
        max_ending_here = 0
        
        #Iterating over the array. 
        for i in range(0, size): 
            #Updating max sum till current index.
            max_ending_here = max_ending_here + a[i]
            
            #Storing max sum so far by choosing maximum between max 
            #sum so far and max sum till current index.
            if (max_so_far < max_ending_here):
                print(max_so_far)
                max_so_far = max_ending_here 
        
            #If max sum till current index is negative, we do not need to add
            #it to result so we update it to zero.
            if max_ending_here < 0: 
                max_ending_here = 0   
        
        #returning the result.
        return max_so_far

print(maxSubArraySum([1,33,40,-89,-96,45,9,-75,-8,2,-8], 11))