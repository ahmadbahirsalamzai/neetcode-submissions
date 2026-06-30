# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, root, maxVal, minVal):
        if not root:
            return True
        
        if not(minVal < root.val < maxVal):
            return False

        l = self.helper(root.left, root.val, minVal)
        r = self.helper(root.right, maxVal, root.val )

        return l and r

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("inf"), float("-inf"))
