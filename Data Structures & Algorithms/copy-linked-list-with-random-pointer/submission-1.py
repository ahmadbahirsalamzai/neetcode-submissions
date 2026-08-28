class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        curr = head.next

        newList = Node(head.val)
        prev = newList

        myMap = {}
        myMap[head] = newList

        # Build copied list and mapping
        while curr:
            newNode = Node(curr.val)
            myMap[curr] = newNode

            prev.next = newNode
            prev = newNode

            curr = curr.next

        currO = head
        currN = newList

        # Set random pointers
        while currO:
            if currO.random:
                currN.random = myMap[currO.random]

            currO = currO.next
            currN = currN.next

        return newList
