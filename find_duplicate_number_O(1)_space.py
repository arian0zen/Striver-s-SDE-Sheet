'''Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2'''

#one obvious way to it is, using hash_map: because we know there are only number 1,2,3,4,...n so a hashkey value for each elements.


def findDuplicate(nums):
    hash_dict = {}
    for i in nums:
        if i not in hash_dict:
            hash_dict[i] = i
        else:
            return i
   
nums = [1,3,4,2,2]
print(findDuplicate(nums))

#but to do it in constant space.. there is an algorithm; floyd's hare and tortoise || using slow and fast pointers

def findDuplicate(nums):
    #getting where fast and slow intersect is the phase 1 of the floyd's algorithm
    slow = 0
    fast = 0
    while True: #looping untill we break, we break when fast and slow pointers intersect
        slow = nums[slow] #moving slow pointer
        fast = nums[fast]
        fast = nums[fast] #fast moves in twice speed than slow! i can write that in one line as well "fast = nums[nums[fast]]"
        if fast == slow: #this is when they intersect, and it is guranteed they will intersect 
            break    
    #now we get slow 's index where they intersect
    #phase 2, in this phase we, declare one more slow at 0 index and then.. move slow2 and slow and see where they intersect, where slow2 intersect slow that will be our ans! as the ques is there must be a duplicate, so there must be a cycle so they must intersect
    slow2 = 0
    while True:
        slow2 = nums[slow2] #moving slow2
        slow = nums[slow] #moving slow
        if slow == slow2: #where they intersect
            return slow #this will always be the answer            

nums = [1,3,4,2,2]
print(findDuplicate(nums))