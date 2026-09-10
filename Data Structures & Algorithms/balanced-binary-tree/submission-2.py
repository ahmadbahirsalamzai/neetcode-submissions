# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# approch: find the height of the left and right subtrees and if the difference is grater than 1 then we return false otherwise tree and we retun the height of the tree to the parent and will a nonlocal function scoped var to keep track off the bool result
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def dfs(node):
            nonlocal isBalanced
            if not node:
                return 0

            # left
            l = dfs(node.left)

            # right
            r = dfs(node.right)

            if abs(l - r) > 1:
                isBalanced = False
            return max(l, r) + 1

        dfs(root)
        return isBalanced
