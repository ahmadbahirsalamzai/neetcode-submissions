# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# in order traversal would give us a list of nodes in an
# asscending order and then return the kth element of the list
class Solution:
    def helper(self, root, k, temp):
        if not root:
            return

        # vist left
        self.helper(root.left, k, temp)

        # add root.val list
        temp.append(root.val)

        # vist right
        self.helper(root.right, k, temp)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        temp = []
        self.helper(root, k, temp)
        return temp[k - 1]
