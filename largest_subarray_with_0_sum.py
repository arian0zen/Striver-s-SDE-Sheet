from asyncio import current_task
from calendar import c


def sumzero(nums):
    res = []  
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum += nums[i]
        if current_sum > 0:
            current_sum = 0
        else:
            res.append(nums[i])
            
    return res   
        
        
        
    
nums = [9, -3, 3, -1, 6, -5]
print(sumzero(nums))
    