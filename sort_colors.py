'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.'''
#there are two approaches for this problem, first we can do is count sort, then a more efficient algorithm if dutch national flag.
# ***count sort*** O(n) || O(1)

def sortColors(nums):
    
    zero = 0
    one = 0
    two = 0
    for i in range (len(nums)):
        if nums[i] == 0:
            zero += 1
        elif nums[i] == 1:
            one += 1
        else:
            two += 1
    for i in range(len(nums)):
        if i < zero:
            nums[i] = 0
        elif i >= zero and i < zero+one:
            nums[i]  = 1
        else:
            nums[i] = 2
    return nums
nums = [2,0,2,1,1,0]
print(sortColors(nums))

#dutch national flag / three pointer approach  O(n) || O(1)

def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid<=high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid] #if mid == 0, swaping it to low, cause it should be at beginning
            mid+=1
            low+=1
        elif nums[mid] == 1: #if mid == 1, keeping it as it is
            mid+= 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid] #if mid == 2, moving it to end
            high -= 1
        
    return nums
    
    
    
nums = [2,0,2,1,1,0]
print(sortColors(nums))