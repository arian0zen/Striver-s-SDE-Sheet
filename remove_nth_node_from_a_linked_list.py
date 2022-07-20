'''


#O(2n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        while current!= None:
            count += 1 #get how many nodes are there
            current = current.next
        remove_count = count - n #which on ehave to remove
        if remove_count == 0: #if we have to remove the very first node
            if head.next != None:
                head.val = head.next.val
                head.next = head.next.next
                return head
            else:
                head = None
                return head
        temp = 0
        node = 0
        dummy = head
        while dummy!= None:
            temp += 1
            if temp == remove_count: #iterate till the Nth node, 
                node = dummy
                break
            dummy = dummy.next
        node.next = node.next.next #then set its next to its next's next
        
        return head
		#as we can see two O(n) iteration 
optimal solution
1. setting as fast pointer to head then moving it to n, from the head
2. if the fast alreadyy at none, that means we needed to remove the head
3. if fast not at the end, we iterate till fast reaches end, and with each iteration we move slow and fast both by one
4. when fast reaches end, the slow's next is the node we needed to delete
5. then we set slow.next = slow.next.next and return head
UPVOTE

#O(n) solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if fast == None: #when we need to remove the head, (first node)
            return head.next
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
        
        '''