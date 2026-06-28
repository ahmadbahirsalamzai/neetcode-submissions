# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if the current node is the divider then return the current node
        if (q.val == root.val or p.val == root.val):
            return root
        
        # if curr node is the divider then return the curr node
        if (p.val < root.val < q.val) or (p.val > root.val > q.val):
            return root

        res = None

        # if both p and q are smaller, then search left side of the tree
        if p.val < root.val > q.val:
            res = self.lowestCommonAncestor(root.left, p, q)

        # if both p and 1 are greater, then search right side of the bst
        if p.val > root.val < q.val:
            res = self.lowestCommonAncestor(root.right, p, q)

        return res