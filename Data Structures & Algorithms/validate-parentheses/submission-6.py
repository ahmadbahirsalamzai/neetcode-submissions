class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) == 0 or len(s) == 1:
        #     return False
        closingSet = {")": "(", "]": "[", "}": "{"}

        stack = []

        for c in s:
            if c in closingSet:
                if stack and stack[-1] == closingSet[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
