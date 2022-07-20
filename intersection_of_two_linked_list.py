# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#added each node of listA in a hash table and checked if any node of listB matches, then return 
#time O(m+n) || O(n)
class Solution:
    def getIntersectionNode(self, headA, headB):
        a_head = headA
        b_head = headB
        listA = {}
        while a_head != None:
            listA[a_head] = True
            a_head = a_head.next
        while b_head != None:
            if b_head not in listA:
                b_head = b_head.next
            else:
                return b_head
        return None
    
'''optimized approach O(max(m,n)) || O(1)'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):  
        head_a = headA
        head_b = headB
        while head_a != head_b:
            if head_a != None:
                head_a = head_a.next
            else:
                head_a = headB
            if head_b != None:
                head_b = head_b.next
            else:
                head_b = headA
        return head_a