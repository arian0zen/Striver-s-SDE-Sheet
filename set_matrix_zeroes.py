#optimized solution!! TIME O(M*N) SPACE O(1)
def setZeroes(matrix) :

    first_col = 1
    for r in range(len(matrix)):
        if matrix[r][0] == 0:
            first_col = 0
        for c in range(1, len(matrix[0])):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0
    # print(matrix)
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                # print(i, j, matrix[i][j], matrix[i][0], matrix[0][j] )
                   matrix[i][j] = 0
                    
    if matrix[0][0] == 0:
        for c in range(len(matrix[0])):
            matrix[0][c] = 0
    if first_col == 0:
        for r in range(len(matrix)):
            matrix[r][0] = 0
    return matrix
            

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix))          

#less optimized, but easy to implement|| TIME O(M*N) SPACE O(M + N) for those two extra arrays

def setZeroes(matrix) :
        row_flag = []
        column_flag = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                # print(r,c)
                if matrix[r][c] == 0:
                    row_flag.append(r)
                    column_flag.append(c)
        # print(row_flag, column_flag)
        
        for r in row_flag:
            for i in range(len(matrix[0])):
                    # print(i)
                matrix[r][i] = 0
        
        for c in column_flag:
            for i in range(len(matrix)):
                matrix[i][c] = 0
        print(matrix)
    
    
    
    
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix)) 
    
