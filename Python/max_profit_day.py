# Input:   price[] = {10, 22, 5, 75, 65, 80}
# Output:  87
# Trader earns 87 as sum of 12, 75 
# Buy at 10, sell at 22, 
# Buy at 5 and sell at 80
# Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
# Output:  100
# Trader earns 100 as sum of 28 and 72
# Buy at price 2, sell at 30, buy at 8 and sell at 80
# Input:   price[] = {100, 30, 15, 10, 8, 25, 80};
# Output:  72
# Buy at price 8 and sell at 80.
# Input:   price[] = {90, 80, 70, 60, 50}
# Output:  0


a = [10, 22, 5, 75, 65, 80]
# a = [2, 30, 15, 10, 8, 25, 80]

bp = a[0]
sp = a[0]
profit = []

for i in range(1, len(a)):
    cur_p, temp = sp - bp, 0
    if(a[i] < bp ):
        bp = a[i]
        sp = a[i]
        temp = sp - bp
        cur_p = max(cur_p, temp)
        # print('BP: ', bp, "SP: ", sp, 'temp: ', temp)
        # print(a[i], ' ', cur_p, ' ', profit)
        
    elif(a[i] > sp):
        sp = a[i]
        
        temp = sp - bp
        # profit.append(cur_p)
        # print('BP: ', bp, "SP: ", sp)
        # print(a[i], ' ', cur_p, ' ', profit)

    elif(a[i] < sp):
        bp = a[i]
        temp = sp - bp
        cur_p = max(cur_p, temp)
        print('Current Profit: ', cur_p)
        profit.append(cur_p)

    # else:
    #     bp = a[i]
    #     sp = a[i]
        
    print('BP: ', bp, "SP: ", sp, 'temp: ', temp)
    # else:
        # print('BP: ', bp, "SP: ", sp)
        # print(a[i], ' ', cur_p, ' ', profit)
        
    
profit.append(temp)
print(sum(profit))
        
        
        

