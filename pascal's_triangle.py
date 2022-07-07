'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:'''


def generate(numRows):
    ans = [[1]*i for i in range(1, numRows+1) ]
    # print(ans)
    for i in range(2, numRows):
        for j in range(1, len(ans[i])-1):
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j] 
    return ans
    
    
numRows = 5
print(generate(numRows))

def generate(numRows):
    ans = []
    # print(ans)
    for i in range(numRows):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(ans[i-1][j-1] + ans[i-1][j])
        ans.append(row)
    return ans
numRows = 5
print(generate(numRows))

