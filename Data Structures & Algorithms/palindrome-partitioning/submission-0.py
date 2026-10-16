class Solution:
    # we can solve this using backtracking
    # approch:
    # we will walk down the descision tree and find all possible sub strings. when we find a substring we will check if it is a plaindrom and then we will add it.
    def isPal(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(start):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                curr = s[start : end + 1]
                if self.isPal(curr):
                    path.append(curr)
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res