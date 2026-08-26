class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sortedLST = []  # (position, speed) => sorted by position

        for i in range(len(position)):
            sortedLST.append([position[i], speed[i]])

        sortedLST.sort(key=lambda x: x[0], reverse=True)

        for i in range(len(sortedLST)):
            t = (target - sortedLST[i][0]) / sortedLST[i][1]

            if not stack:
                stack.append(t)
            else:
                if stack[-1] < t:
                    stack.append(t)

        return len(stack)
