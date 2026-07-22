class Solution:
    def climbStairs(self, n: int) -> int:
        # Time: 
        # Space: 
        one, two = 1, 1

        # exclude the last two elements because the number of
        # ways to get from the second last to the last item 
        # would always be 1 because 2 would overflow. 
        for i in range(n-1):
            temp = one

            one = one + two
            two = temp
        return one
