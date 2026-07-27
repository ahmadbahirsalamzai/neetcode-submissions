class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def isPalindrom(l, r):
            nonlocal count
            while l >= 0 and r < len(s) and s[r] == s[l]:
                count += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            isPalindrom(i, i)
            isPalindrom(i, i + 1)

        return count
