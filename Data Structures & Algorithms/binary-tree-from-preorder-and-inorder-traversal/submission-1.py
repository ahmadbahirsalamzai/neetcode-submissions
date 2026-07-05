# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time: O(n^2)
# space: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # take the first element of the preorder and make the root at current level
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # construct left subtree
        root.left = self.buildTree(preorder[1:1 + mid], inorder[:mid])
        
        #construct the right subtree
        root.right = self.buildTree(preorder[1 + mid:],inorder[1+mid:] )

        return root