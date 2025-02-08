# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        explored = set()

        while head:
            if head in explored:
                return True
            else:
                explored.add(head)
            head = head.next    

        return False