'''Problem Statement
You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.
Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N] which appears in the array twice and another number M in the range [1, N] which is missing from the array.
Your task is to find the missing number (M) and the repeating number (R).
For Example:
Consider an array of size six. The elements of the array are { 6, 4, 3, 5, 5, 1 }. 
The array should contain elements from one to six. Here, 2 is not present and 5 is occurring twice. Thus, 2 is the missing number (M) and 5 is the repeating number (R).'''
def missingAndRepeating(arr):
    n = len(arr)
    r = 0
    m = 0
    for i in arr:
        if arr[abs(i)-1] < 0:
            r = abs(i)
        else:
            arr[abs(i)-1] = -arr[abs(i)-1]
    print("the duplicate number is :", r)        
    
    for i in arr:
        if i > 0:
            m = arr.index(i) + 1
    print ("the missing number is :")
    return m
            


arr = [6, 4, 3, 5, 5, 1]
print(missingAndRepeating(arr))

# ***approach***
'''Marking Elements
The idea is to traverse the array and mark the visited elements.

While traversing the array, we will use the absolute value of every element as an index and make the value at this index as negative to mark it visited. For example, for element 3, we will make the value at index 2 as negative ( since the array is 0-indexed ). For any element in the array, if the element at the index {element - 1} is already marked negative, then this is the repeating element. 

To find the missing number, we will traverse the array again and look for a positive value. The index at which we find the positive value is our missing number because that index is not present in the array as an element.  

 

For Example: Consider the array Arr = { 1, 5, 2, 2, 3 }. 

Now we will traverse the array and mark the visited numbers as follows: 

At index 0, we encounter 1. To mark this element as visited, Arr[1 - 1] = - Arr[1 - 1].
Current array Arr: {-1, 5, 2, 2, 3}. 

At index 1, we encounter 5. To mark this element as visited, Arr[5 - 1] = - Arr[5 - 1].
Current array Arr: {-1, 5, 2, 2, -3}. 

At index 2, we encounter 2. To mark this element as visited, Arr[2 - 1] = - Arr[2 - 1].
Current array Arr: {-1, -5, 2, 2, -3}. 

At index 3, again we encounter 2.
Here, the element at index 1 (2 - 1), is already negative. It means we have already visited it. Thus, we have found our repeating number ‘R’ which is 2. 

Current array Arr: {-1, -5, 2, 2, -3}. 

At index 4, we encounter 3. To mark this element as visited, Arr[3 - 1] = - Arr[3 - 1].
Current array Arr: {-1, -5, -2, 2, -3}. 

To find the missing number ‘M’, we will again traverse the array.
We will find that the element at index 3 is the only positive element. It means that the missing number is 3 + 1 = 4.
So, our missing number ‘M’ is 4 and the repeating number ‘R’ is 2. '''