# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# approch: perform a dfs and keep track of two things: max value down a path and also the count
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, currMax):
            nonlocal count

            if not node:
                return

            if node.val >= currMax:
                count += 1
            if node.val > currMax:
                currMax = node.val

            # left
            dfs(node.left, currMax)

            # right
            dfs(node.right, currMax)

        dfs(root, float("-inf"))

        return count
