'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.'''

#at first we are transposing the matrix, by that we are allocating rows to columns, and columns to matrix, than we are just reversing the transposed matrix's rows



def rotateMatrix (matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
             #these two nested loops are for transposing
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
        #this loop is for reversing the rows of the matrix
    return matrix

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotateMatrix(matrix))
