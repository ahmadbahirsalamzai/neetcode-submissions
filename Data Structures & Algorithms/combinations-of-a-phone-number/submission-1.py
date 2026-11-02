class Solution:
    # time: O(n * n^4)
    # space: O(n)
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        lenDigits = len(digits)
        charMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(i, curr):
            if len(curr) == lenDigits:
                # append curr to res
                res.append(curr)
                return

            # for each current digit make a recursive call
            # you cannot not take a digit
            for k in charMap[digits[i]]:
                dfs(i + 1, curr + k)

        if digits:
            dfs(0, "")

        return res
