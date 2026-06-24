# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle el
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None  # split the list

        # Reverse the second half
        temp = None
        while curr:
            nextCurr = curr.next
            curr.next = temp
            temp = curr
            curr = nextCurr

        # Now, we have two list
        """ 
            Example: 
            [0, 1, 2, 3, 4, 5, 6]

            head --> [0, 1, 2, 3]
            temp --> [4, 5, 6]
        """
        curr1 = head
        curr2 = temp

        while curr2:
            # Save the next nodes for both halves
            next1 = curr1.next
            next2 = curr2.next

            # Connect curr1 to curr2, then curr2 to next1
            curr1.next = curr2
            curr2.next = next1

            # Move pointers forward for the next iteration
            curr1 = next1
            curr2 = next2
