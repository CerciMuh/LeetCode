# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        left = head 
        right = head 

        for i  in range(n):
            right = right.next 
        #now right is n spaces from left 

        if right is None:
            return head.next #if we are removing the element 

        while (right.next is not None):
            
            left = left.next # here left is n spaces from end
            right = right.next #we keep traversing this till right reaches the end 

        left.next = left.next.next #left, left.next, left.next.next we skip the left.next

        return head        