from tracemalloc import start


def lengthOfLongestSubstring(s):
    left = 0
    count = 0
    hash_set = set()
   
    for right in range(len(s)):  
        while s[right] in hash_set:
            hash_set.remove(s[left])
            left += 1
        hash_set.add(s[right])
        # count += 1
        count = max(count, right - left + 1)
            
    return count
        
    # n = len(s) - 1
    # print("length is", n)
      
s =  "dvdf"
print(lengthOfLongestSubstring(s))
        