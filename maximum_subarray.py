"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 """

def maxSubArray(nums):
    max_sum = min(nums)
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


nums = [1, 2, 7, -4, 3, 2, -10, 9, 1]
print(maxSubArray(nums))



#brute force goes BRRRRRRR BRRRRRRRRRR
# def maxSubArray(nums):
#     max_sum = 0
#     for i in range(1, len(nums)+1):
#         max_count = nums[i-1]
#         count = nums[i-1]
#         for j in range(i, len(nums)):
#             count += nums[j]
#             max_count = max(max_count, count) 
#         max_sum = max(max_sum, max_count)
#     return max_sum
        