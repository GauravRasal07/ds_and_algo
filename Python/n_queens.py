N = int(input('Enter the value of n: '))
'''The function n_queen() takes in the number of queens to be placed, the result list, and the chess
    board. 
    
    If the number of queens to be placed is equal to the number of rows in the chess board, then the
    result list is appended with the chess board and the number of solutions is incremented. 
    
    If the number of queens to be placed is not equal to the number of rows in the chess board, then the
    function iterates through the rows of the chess board. 
    
    If the position is safe and the position is not already occupied by a queen, then the position is
    occupied by a queen. 
    
    The function n_queen() is called again with the number of queens to be placed incremented by 1, the
    result list, and the chess board. 
    
    The position is then freed up. 
    
    The
    
    :param i: row
    :param j: column
    :param chase_board: The board that is being used to solve the problem
    :return: a list of lists.
'''

chase_board = [[0] * N for _ in range(N)]
solutions = 0
# empty_board = [[0] * N for _ in range(N)]

def isSafe(i, j, chase_board):
    for k in range(N):
        if chase_board[i][k] == 1 or chase_board[k][j] == 1:
            return False

    for a in range(N):
        for b in range(N):
            if a + b == i + j or a - b == i - j:
                if chase_board[a][b] == 1:
                    return False
        
    return True

def n_queen(n, res, chase_board):
    if n == N:
        res.append(chase_board)
        solutions += 1
        # chase_board = empty_board
        return

    for i in range(N):
        # for j in range(N):
        if isSafe(i, n, chase_board) and chase_board[i][n] != 1:
            chase_board[i][n] = 1

            n_queen(n+1, res, chase_board)

            chase_board[i][n] = 0

    # return False

def no_of_solutions(n):
    res = []
    n_queen(0, res, chase_board)

    return res

print(no_of_solutions(N))
print("The number of solutions are: ", solutions)

# print("The solution is: ")
# for i in range(N):
#     for j in range(N):
#         print(chase_board[i][j], end=" ")
#     print()