class Solution:
    # We can solve this problem using backtracking.
    # Approach:
    # We explore the decision tree to find all possible substrings.
    # For each substring, we check whether it is a palindrome.
    # If it is, we add it to the current partition.

    # space: O(n) excluding output
    # Time: O(n^2 * 2^n)
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
