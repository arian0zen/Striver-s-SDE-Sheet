#i pointer : first number
#j pointer : second number
#k pointer : third number
#end pointer : last number

#time O(n*^3) space O(n)

def fourSum(nums, target):
    res = set()
    n = len(nums)
    if n == 0:
        return res
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:  #this line to get check if we are checking duplicates! if duplicates found, simply skip that iteration
            continue
            
        target3 = target - nums[i]
        for j in range(i+1, n):
            target2 = target3 - nums[j]
            k = j+1
            end = n-1
            while k < end:
                sum_now = nums[k] + nums[end]
                if sum_now < target2:
                    k += 1
                elif sum_now > target2:
                    end -= 1
                else:
                    res.add((nums[i],nums[j],nums[k],nums[end]))
                    k+=1
    return res

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))
