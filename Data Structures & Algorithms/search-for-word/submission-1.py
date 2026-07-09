class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(x, y, i):
            if i == len(word):
                return True

            if x >= len(board) or x < 0 or y >= len(board[0]) or y < 0 or board[x][y] != word[i]:
                return False
            temp = board[x][y]
            board[x][y] = '#'

            # check the left el
            l = dfs(x, y - 1, i + 1)

            # check the right el
            r = dfs(x, y + 1, i + 1)

            # check the bottom el
            b = dfs(x + 1, y, i + 1)

            # check the top el
            t = dfs(x - 1, y, i + 1)
            board[x][y] = temp

            return l or r or b or t

        # call the dfs method
        for j in range(len(board)):
                for x in range(len(board[0])):
                    #print(j,x)
                    if dfs(j,x,0):
                        return True


        return False