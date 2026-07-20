class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n - 1 or len(edges) < n-1:
            return False

        # build a map: curr -> child nodes are
        myMap = {i: [] for i in range(n)}
        for curr, child in edges:
            myMap[curr].append(child)
            myMap[child].append(curr)

        # set to keep track of the current path
        visited = set()

        # do a dfs starting
        def dfs(curr, par):
            # return False which means that there is an isolated edge
            if curr in visited:
                return False

            # Add the curr node to visited
            visited.add(curr)

            # make a dfs call for all the neighboring nodes of the par node
            for nei in myMap[curr]:
                if nei == par:
                    continue
                if not dfs(nei,curr):
                    return False

            # return true if all nodes visited
            return True

        # make one dfs call...
        return dfs(0, -1) and len(visited) == n
