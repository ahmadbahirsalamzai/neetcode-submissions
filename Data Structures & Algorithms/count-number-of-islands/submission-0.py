class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(i, j):
            # check the bound in the base case
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1 or grid[i][j] == "0":
                return

            # mark connected islands as 0 (visited):
            grid[i][j] = "0"

            # if right element is 1 make a dfs call with it:
            dfs(i, j + 1)

            # if left element is 1 make a dfs call with it:
            dfs(i, j - 1)

            # if top element is 1 make a call with it:
            dfs(i - 1, j)

            # bottom elemen is 1 make a call with it:
            dfs(i + 1, j)

            return

        # do dfs for each pice of land (1) and don't make a call to dfs fro water(0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if the curr el. is 1 make a dfs call.
                if grid[i][j] == "1":
                    print(grid)
                    count += 1
                    dfs(i, j)

        return count
