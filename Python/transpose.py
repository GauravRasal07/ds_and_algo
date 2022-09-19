def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])

    
    res = [[0 for i in range(rows)] for j in range(cols)]
    # print(res)
    for i in range(rows):
        for j in range(cols):
            print(i, j)
            if i != j:
                res[j][i] = mat[i][j]
            else:
                res[i][j] = mat[i][j]

    return res
    
    # else:
    #     res = [[0] * cols] * rows
    #     return res




mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(mat))