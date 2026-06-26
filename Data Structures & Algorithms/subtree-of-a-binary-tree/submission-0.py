# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # method for isSameTree
    def isSame(self, root1, root2):
        if not root1 and not root2:
            return True

        # if current nodes aren't the same return false
        if not (root1 and root2 and root1.val == root2.val):
            return False

        # recursive calls
        l = self.isSame(root1.left, root2.left)
        r = self.isSame(root1.right, root2.right)

        return l and r

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # this is for an empty tree
        if not root:
            return False

        found = self.isSame(root, subRoot)
    
        # recursive call left
        l = self.isSubtree(root.left, subRoot)

        # recursive call right
        r = self.isSubtree(root.right, subRoot)

        # not found on the right or left
        return found or r or l
