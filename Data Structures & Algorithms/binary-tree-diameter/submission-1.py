# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # time = O(n)
        # Space = O(h)
        total = 0

        def dfs(root):
            nonlocal total
            if not root:
                return 0
            
            # left 
            l = dfs(root.left)

            #right 
            r = dfs(root.right)
            total = max(total, l + r)
            return max(l, r) + 1

        dfs(root)

        return total
        
