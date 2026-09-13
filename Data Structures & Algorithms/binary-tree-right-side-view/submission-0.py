# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# approch: if we perform bfs on any tree, in every level the the last element will give use the element that is visiable from the right hand side. Therefore, if we perform a BFS on this tree and keep adding the last element in each level to a res list, we will get the right side view.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque([root])
        q.append(root)

        while q:
            rightside = None
            qlen = len(q)
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val)

        return res

            