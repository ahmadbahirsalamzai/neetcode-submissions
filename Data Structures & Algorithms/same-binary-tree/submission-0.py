# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case to handle none's
        if not p and not q:
            return True
        
        # check current nde equality
        if not(p and q and p.val == q.val):
            return False
        
        # recursive call left
        l = self.isSameTree(p.left, q.left)

        # recursive call right
        r = self.isSameTree(p.right, q.right) 

        # compare and return 
        return l and r