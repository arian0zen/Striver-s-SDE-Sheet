#dynamic programming recursive, dp memory | time O(m*n) | space O(n*m)

def uniquePaths(m, n) :
    count = 0
    dp = [[-1]*n for i in range(m)]
    # print(dp)
    def recursion(i, j, m, n):
        if (i == (m-1)) and (j == (n-1)):
            return 1
        elif (i >= m) or (j >= n):
            return 0
        # print(i,j)
        if dp[i][j] != -1:
            return dp[i][j]
        else:
            dp[i][j] = recursion(i+1, j, m, n) + recursion(i, j+1, m, n)
            return dp[i][j]
        
    return recursion(0, 0, m, n)
 
 
#non recursive dynamic programming | time O(n*m) | space O(n) 
   
print(uniquePaths(3,7))

def uniquePaths(m, n) :
    last_row = [1]*n
    for i in range(m-1):
        newRow = [1]*n
        for j in reversed(range(n-1)):
            newRow[j] = newRow[j+1]  + last_row[j] #this can be done without the new array, i can just update the previous arrat last_row|| last_row[j] = last_row[j+1] + last_row[j]
        last_row = newRow
    return last_row[0]
    
#combinatrics approach nCr approach | time O(m-1) ~ O(n) | space o(1)    
     
print(uniquePaths(3,7))

def uniquePaths(m, n):
    N = m+n-2
    r = m-1
    ans = 1
    for i in range(1, r+1):
        ans = (ans*(N-r+i)) // i
    return ans
    
    
print(uniquePaths(3,7))