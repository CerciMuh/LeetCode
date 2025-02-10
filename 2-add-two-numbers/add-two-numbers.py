# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        listOneArray= []
        listOneNumber =""
        listTwoArray=[]
        listTwoNumber=""

        while l1:
            listOneArray.append(l1.val)
            l1 = l1.next
        listOneNumber = "".join(map(str,listOneArray))
        while l2:
            listTwoArray.append(l2.val)   
            l2=l2.next
        listTwoNumber = "".join(map(str,listTwoArray))

        listOneNumberRev = ""
        for i in listOneNumber [::-1]:
            listOneNumberRev = listOneNumberRev + i

        listTwoNumberRev=""
        for i in listTwoNumber [::-1]:
            listTwoNumberRev = listTwoNumberRev + i
        combinedSum = int(listOneNumberRev)+int(listTwoNumberRev)

        dummy = ListNode(0)
        current = dummy
        for i in str(combinedSum)[::-1]:
            current.next = ListNode(int(i))
            current = current.next

        return dummy.next 
            