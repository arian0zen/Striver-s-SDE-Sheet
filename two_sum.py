def twoSum(nums, target):
    hash_dict = {}
    for each, number in enumerate(nums):
        difference = target - number
        if difference in hash_dict:
            return [hash_dict[difference], each]
        else:
            hash_dict[number] = each
nums = [1,3,4,6]
target = 7
print(twoSum(nums, target))