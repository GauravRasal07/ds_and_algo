def findMaxMin(arr) :
    min = 0 
    max = 0
    for i in arr :
        if(i < min) :
            min = i

        elif(i > max) :
            max = i

    print('Minimum is: ', min, 'Maximum is: ', max)

findMaxMin([-1, 2, 5, 66, 99])