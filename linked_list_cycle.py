'''storing each node in hash table then if any node is found same as present in the hash table return true'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        hash_dict = {}
        while head!= None:
            if head not in hash_dict:
                hash_dict[head] = True
                head = head.next
            else:
                return True
        return False

O(n) || O
'''using slow and fast pointer, if there is cycle then fast must collide with slow, fast moves twice as fast as slow. fast = fast.next.next'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast!= None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
# O(n) || O(1)
