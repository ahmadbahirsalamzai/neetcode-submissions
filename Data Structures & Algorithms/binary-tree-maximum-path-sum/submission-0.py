# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.currMax = float("-inf")
        
        def getMax(node):
            if not node:
                return 0

            l = max(0, getMax(node.left))
            r = max(0, getMax(node.right))
            

            pathSum = l + r + node.val
            self.currMax = max(self.currMax, pathSum)

            # pick left or right
            return max(r,l) + node.val
        getMax(root)
        return self.currMax