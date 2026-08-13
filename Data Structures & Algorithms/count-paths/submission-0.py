class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * n for _ in range(m)]

        # i = n -> used to itterate through the  rows
        # j = m -> update in the dfs calls
        def dfs(i, j):
            # check the bouds, if we are out of the bounds return 0
            # might not be necessery
            if i == m or j == n:
                return 0
            if i == m-1 and j == n-1:
                return 1

            if cache[i][j] != -1:
                return cache[i][j]

            # move down right and move down
            cache[i][j] = dfs(i+1,j) + dfs(i, j+1)
            
            return cache[i][j]
        res = dfs(0, 0)
        return res
