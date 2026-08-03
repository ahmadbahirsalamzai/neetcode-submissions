"""
Use a stack to keep track of the split points
and if when finished iterating the string
and the top of ths stack is equal to the length then return treu, else
return fasle
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        # check if any of the words match the word from 0-i
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            

            # run a for loop for each word
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    if dfs(i + len(word)):
                        return True
                memo[i] = False
            return False

        return dfs(0)
