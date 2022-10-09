'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into one single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.'''

def merge(nums1, m, nums2, n):
    #this approach will work only if nums1 alreay have the empty space to fit nums2 || time O(n*m) || space O(1)

    end = len(nums1)-1 #setting up the end pointer! also m-1 is first array 's last pointer and n-1 is second array 's last pointer
    while n > 0 and m > 0 : #loop while both of them are not empty
        if nums1[m-1] > nums2[n-1]: #if nums1 's last elem is greater than nums2's last elem.. then adding that to merged array's last! that means that is the largest elem available
           nums1[end] = nums1[m-1]
           m -= 1 #moving the pointer || well, we are looping in reverse order
           end -= 1
        else:
            nums1[end] = nums2[n-1] #else adding 2nd aray's last elem
            n -= 1
            end -= 1
    while n > 0 : #this loop is to check if any elements are remaining in the 2nd array!! if yes.. then adding them all
        nums1[end] = nums2[n-1]
        n -= 1
        end -= 1
    return nums1
        
    
    
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))

#what if there were not extra space in nums1, in that case we gotta use the swap .... 
def merge(nums1, m, nums2, n):

    for i in range(m):
        if nums1[i] > nums2[0]:
            nums1[i], nums2[0] = nums2[0], nums1[i]
            nums2.sort()
    return nums1, nums2
    


nums1 = [1,2,3]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))













    # nums1 = nums1[0:m]
    # nums1 = nums1 + nums2
    # nums1.sort()
    # return nums1
    
