class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(numsList):
            prev1, prev2 = 0, 0

            for i in range(len(numsList)):
                temp = prev1
                prev1 = max(prev1, prev2 + numsList[i])
                prev2 = temp

            return prev1

        # res would be equal to the max of nums excluding the last element and nums of excluding the first element
        res = max(helper(nums[:-1]), helper(nums[1:]))
        return res
