class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1

        for curr in nums:
            temp = currMax * curr
            currMax = max(currMax * curr, currMin * curr, curr)
            currMin = min(temp, currMin * curr, curr)
            res = max(currMax, res)
        return res
