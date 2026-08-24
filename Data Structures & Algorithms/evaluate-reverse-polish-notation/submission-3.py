class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time = O(n)
        # Space = O(n)

        # push to the stack until the loop lands on an operator
        stack = []

        for curr in tokens:
            if curr in "+-*/":
                num1 = stack.pop()
                num2 = stack.pop()

                if curr == "+":
                    stack.append(num1 + num2)
                if curr == "-":
                    stack.append(num2 - num1)
                if curr == "*":
                    stack.append(num1 * num2)
                if curr == "/":
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(curr))
        return stack[-1]
