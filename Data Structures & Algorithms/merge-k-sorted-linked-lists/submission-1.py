# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l1 = []
        for l in lists:
            curr = l
            while curr:
                l1.append(curr.val)
                curr = curr.next
        l1.sort()

        res = ListNode()
        curr = res
        for val in l1:
            curr.next = ListNode(val)
            curr = curr.next

        return res.next
