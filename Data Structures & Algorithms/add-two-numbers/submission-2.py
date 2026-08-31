# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # time = O(max(N, M))
        # space = O(max(N, M) + 1)

        curr1 = l1
        curr2 = l2
        carry = 0

        dummy = ListNode(0)
        currRes = dummy

        while carry > 0 or curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            # 9 + 5 = 14
            total = val1 + val2 + carry

            carry = 0
            val = total % 10
            carry = total // 10

            currRes.next = ListNode(val)
            currRes = currRes.next

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        return dummy.next
