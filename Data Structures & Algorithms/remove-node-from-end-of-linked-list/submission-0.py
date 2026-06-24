# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenList = 0
        curr = head

        while curr:
            lenList += 1
            curr = curr.next

        # subtract 1 from lenList to land on the node before the target node
        lenList = (lenList - n) - 1
        if lenList == -1:
            return head.next

        curr1 = head
        for i in range(lenList):
            curr1 = curr1.next
            
        # Now curr1 is poiting to the element before the nth element
        curr1.next = curr1.next.next
        return head



        
