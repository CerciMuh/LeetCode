# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create an empty linked list 
        #get a while loop with two conditions head (curr1) of list 1 and head(curr2) of list two 

        #inside the while loop we will compare the two nodes now 
        #if curr1 < curr2 insert curr1 and advance it
        #if curr 2 < curr1 insert curr2 and advance it. 
        #we will keep doing this till one list finished and if one list finished before the other, just insert the other fully 
        
        sortedListHead = ListNode(0)
        sortedListTail = sortedListHead
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val<curr2.val:
                sortedListTail.next = curr1
                sortedListTail = sortedListTail.next 
                curr1=curr1.next
            else:
                sortedListTail.next = curr2
                sortedListTail = sortedListTail.next
                curr2=curr2.next
        if curr1:
            sortedListTail.next =curr1
        else: 
            sortedListTail.next = curr2

        return sortedListHead.next
