class Solution:
    # uderstanding:
    # 0 -> means water
    # 1 -> mean land
    # given grid 2d materix surrounded by water

    # approch: keep track of resMax and currMax
    # and then explore all four directions when you land on a land.
    # do an in place marking of the visited sides and make 1 when taken into account
    # we mark the visited 1 becuase we want to skip when iteratin over each row
    # nested for loop calling dfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        resMax = 0
        currMax = 0
        numRows = len(grid)
        numCols = len(grid[0])

        # i -> row or outer list
        # j -> col or inner list
        def dfs(i, j):
            nonlocal currMax, resMax
            # check the bounds
            if i < 0 or i >= numRows or j < 0 or j >= numCols or grid[i][j] == 0:
                return

            currMax += 1
            grid[i][j] = 0

            # left
            dfs(i, j - 1)

            # right
            dfs(i, j + 1)

            # top
            dfs(i + 1, j)

            # bottom
            dfs(i - 1, j)

            resMax = max(currMax, resMax)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    currMax = 0

        return resMax
