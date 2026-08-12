# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# approch: make a string that has the inorder traversal of the tree
# and sperate items by a #


class Codec:
    i = 0

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "@"

        # visit left
        left = self.serialize(root.left)

        # visite current
        curr = root.val

        # right
        right = self.serialize(root.right)

        res = f"{curr}#{left}#{right}"

        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # split the string by "#"
        sList = data.split("#")

        root = self.buildTree(sList)
        return root

    def buildTree(self, nList):
        if self.i >= len(nList):
            return None

        currVal = nList[self.i]
        self.i += 1

        if currVal == "@":
            return None

        node = TreeNode(int(currVal))
        node.left = self.buildTree(nList)
        node.right = self.buildTree(nList)

        return node
