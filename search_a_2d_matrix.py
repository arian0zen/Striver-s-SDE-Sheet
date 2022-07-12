'''Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.'''

#what i am doing is running binary search through the first column and getting the note of on which row the target should be
#then again binary search through that row, to check if the target exits
#time complexity when m = rows; n = columns || O(log(n)) + O(log(m)) ~ O(log(n)) || i am not sure about that.. if any of you can confirm me please

def searchMatrix(matrix, target):
    n = len(matrix[0])-1
    row_index  = -1
    left = 0
    right = len(matrix)-1
    while left <= right:
        mid = (left + right) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target and matrix[mid][n] >= target:
            row_index = mid
            break
        elif matrix[mid][0] > target:
            right = mid -1
        else:
            left = mid+1
            
    if row_index == -1:
        return False
    else:
        start = 0
        end = len(matrix[row_index])
        while start <= end:
            mid = (start + end) // 2
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] > target:
                end = mid-1
            else:
                start = mid+1
        return False
            
        


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(searchMatrix(matrix, target))

'''also As it is clearly mentioned that the given matrix will be row-wise and column-wise sorted, we can see that the elements in the matrix will be in a monotonically increasing order. So we can apply binary search to search the matrix. Consider the 2D matrix as a 1D matrix having indices from 0 to (m*n)-1 and apply binary search. Below the available image is the visual representation of the indices of 3*4 matrix.'''
def searchMatrix(matrix, target):
    columns = len(matrix[0])
    left, right = 0, (len(matrix) * columns) - 1
        
    while left <= right:
        middle = (left + right) // 2
        row, column = middle // columns, middle % columns

        if matrix[row][column] == target:
            return True
        elif matrix[row][column] > target:
            right = middle - 1
        else:
            left = middle + 1
 
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(searchMatrix(matrix, target))