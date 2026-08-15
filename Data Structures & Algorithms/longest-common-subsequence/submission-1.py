class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        cache = [[-1] * n  for _ in range(m)]

        def dfs(i,j):
            if i >= m or j >= n:
                return 0

            if cache[i][j] != -1:
                return cache[i][j]
            
            # if both curr element are equal then 1 + dfs(advance both pointers)
            if text1[i] == text2[j]:
                cache[i][j] = 1 + dfs(i+1, j+1)

            # if curr elements don't match then don't add 1 and addvance one of the pointer
            else:
                cache[i][j] = max(dfs(i, j+1), dfs(i+1, j)) 
            
            return cache[i][j]
        
        return dfs(0,0)
                

            
        
        
