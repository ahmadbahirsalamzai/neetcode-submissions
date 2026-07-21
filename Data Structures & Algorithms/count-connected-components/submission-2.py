class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0

        # build an adjacency list map
        myMap = {i: [] for i in range(n)}
        for node, nei in edges:
            myMap[node].append(nei)
            myMap[nei].append(node)

        # visited set to keep track of the items visited
        visited = set()

        # dfs: traverse through a component and add the visited items to the set
        # and incremen teh res counter
        def dfs(currNode):
            if currNode in visited:
                return

            visited.add(currNode)
            for node in myMap[currNode]:
                dfs(node)

        # call dfs per one item from each component
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res
