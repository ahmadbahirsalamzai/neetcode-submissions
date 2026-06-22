# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Space: O(n)
# Time: O(n)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()

        curr = list1
        curr2 = list2
        curr3 = list3
        
        while curr != None and curr2 != None:
            #current value of l1 is smaller than l2 append to the 
            if curr.val < curr2.val:
                curr3.next = curr
                curr = curr.next
            else: 
                curr3.next = curr2
                curr2 = curr2.next
                
            curr3 = curr3.next 
        curr3.next = curr if curr != None else curr2

        return list3.next
