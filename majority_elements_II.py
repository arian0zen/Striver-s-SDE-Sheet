#this is the hash_map approach || time o(n) ||| space O(n)

def majorityElement(nums):
    n = len(nums)
    hash = {}
    for i in nums:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
                
    ans = []
    for x in hash:
        if hash[x] > n//3:
            ans.append(x)
    return ans        

nums = [3,2,3]
print(majorityElement(nums))

#moore voting algorithm extended || Time O(n) Space O(1)
def majorityElement(nums):
    n = len(nums)
    count1 = 0
    count2 = 0
    nums1 = None
    nums2 = None
    for i in nums:
        if i == nums1:
            count1 += 1
        elif i == nums2:
            count2 += 1
        elif count1 == 0:
            nums1 = i
            count1 = 1
        elif count2 == 0:
            nums2 = i
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    # return nums1, nums2
    ans = [] #taking this array may seem like oh oh lol this is O(n) time!! noh bruh.. we are surely appending only two elements in the array that are taking constant space
    if nums.count(nums1) > n//3:
        ans.append(nums1)
    if nums.count(nums2) > n//3:
        ans.append(nums2)
    return ans
    
nums = [11,33,33,11,33,11]
print(majorityElement(nums))