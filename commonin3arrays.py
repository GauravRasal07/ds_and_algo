def commonElements (A, B, C, n1, n2, n3):
        # your code here
        
        res = []
        
        i = 0
        j = 0
        k = 0
        
        while(i < n1 and j < n2 and k < n3):
            
            a = A[i]
            b = B[j]
            c = C[k]
            
            if(a == b == c and a not in res):
                res.append(a)
                i += 1
                j += 1
                k+=1
                
            elif(a < b):
                i += 1
                
            elif(b < c):
                j += 1
                
            else:
                k += 1
                
        return res

commonElements([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120], 6, 5, 8)