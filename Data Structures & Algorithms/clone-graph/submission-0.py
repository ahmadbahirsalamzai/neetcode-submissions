"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        myMap = dict()

        def dfs(currNode):
            # if a new node is created for this node then return it
            if currNode in myMap:
                return myMap[currNode]

            # create a new Node
            copy = Node(currNode.val)

            # add the copy of the new node to myMap
            myMap[currNode] = copy

            # iterate through child currNode and append the new child nodes to copy
            for i in currNode.neighbors:
                copy.neighbors.append(dfs(i))

            return copy

        return dfs(node) if node else None
