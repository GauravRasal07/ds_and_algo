import time

def subArrayExists(arr,n):
        ##Your code here
        #Return true or false
        cons_sums = set()
        sums = 0
        startTime = time.time()
        for i in arr:
            sums += i
            if(sums in cons_sums or sums == 0):
                return 1
                
            cons_sums.add(sums)
            
        return 0

subArrayExists([1, 4, -2, -2, 5, -4, 3], 7)