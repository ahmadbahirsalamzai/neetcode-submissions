class Solution:
    # INF : land cell -> can be traversed
    # 0   : a treasure chest -
    # -1  : water cell -> can't be traversed

    # goal: fill each land cell with the distance to its ##nearest## treasure chest.
    # if a land cell cannot reach a treasure chest then thevalue should remain INF.
    # the graph can traversed up, down, left, right.
    # modify the grid in-place.
    # u can't change -1 and you can't traverse in that direction.

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()

        # adding all the treasure chest as a starting point to the q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
