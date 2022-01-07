def maxSubArraySum(arr,N):
        max_sum=arr[0]
        cur_sum=arr[0]
        
        for i in range(1,N):
            if(cur_sum<0):
                cur_sum=0
            cur_sum=cur_sum+arr[i]
            if(cur_sum>max_sum):
                max_sum=cur_sum
        return max_sum

maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3], 8)