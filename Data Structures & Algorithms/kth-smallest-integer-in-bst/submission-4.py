# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# in order traversal would give us a list of nodes in an
# asscending order and then return the kth element of the list
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.k = k

        def helper(root):
            if not root or self.res != None:
                return

            # vist left
            helper(root.left)

            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return

            # vist right
            helper(root.right)

        helper(root)
        return self.res
