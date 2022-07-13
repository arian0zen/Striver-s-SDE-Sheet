'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3'''

#first approach we are using hash_map to keep count of elements frequency
#if any elements goes beyond n//2 mark, we return
#time O(n) || space O(n)



from tkinter import E


def majorityElement(nums):
    n = len(nums)
    hash_dict = {}
    for i in range(n):
        if nums[i] not in hash_dict:
            hash_dict[nums[i]] = 1
        else:
            hash_dict[nums[i]] += 1
        if hash_dict[nums[i]] > (n//2):
            return nums[i]
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))

#this same code can be written as, 
'''    def majorityElement(nums):
            counts = collections.Counter(nums)
            return max(counts.keys(), key=counts.get)'''
            
            
#the optimized approach is boyer-moore voting algorithm!!
#intuition and approach explained in notebook (!personal note)
#time O(n) || space O(1)
def majorityElement(nums):
    count = 0
    element = 0
    for i in nums:
        if count == 0:
            element = i
        if i == element:
            count += 1
        else:
            count -+ 1
    return element
    
    
    
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))