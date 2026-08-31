# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# approch:
# Itterate through the lists
# consider the folloiwng tow cases where an overflow can happen
# 1) overflow at the begging or in the middle.
# 2) overflow in the middle.
#


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

            # re initlize back to zero so that no carry added to the next number mutiple times
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
