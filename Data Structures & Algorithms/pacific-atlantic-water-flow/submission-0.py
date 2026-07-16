class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        # Keep track of the items that can flow to the pacific/atlantic
        pacific, atlantic = set(), set()

        # do dfs and find if any of the adj cells are smaller than the curr cell if so then add that cell.
        def dfs(i, j, visited, prev):
            # if i or j is out of bound or current value is samller than the pre value than we return
            if (
                (i, j) in visited
                or i < 0
                or i > ROWS - 1
                or j < 0
                or j > COLS - 1
                or heights[i][j] < prev
            ):
                return

            # add the current value to the visited set
            visited.add((i, j))

            # call dfs with the right child
            dfs(i, j + 1, visited, heights[i][j])

            # call dfs with the left child
            dfs(i, j - 1, visited, heights[i][j])

            # call dfs with the bottom child
            dfs(i + 1, j, visited, heights[i][j])

            # call dfs with the top child
            dfs(i - 1, j, visited, heights[i][j])

        # run a dfs search for the first row (all nodes are in pacific.) and the last row (all nodes are in atlantic)
        for i in range(COLS):
            # pacific: make a dfs function call with the first row cols
            dfs(0, i, pacific, heights[0][i])
            # atlantic: make a dfs function call with elements of the last row cols
            dfs(ROWS - 1, i, atlantic, heights[ROWS - 1][i])

        for j in range(ROWS):
            # pacific
            dfs(j, 0, pacific, heights[j][0])
            # atlantic
            dfs(j, COLS - 1, atlantic, heights[j][COLS - 1])

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        return res