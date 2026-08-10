class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True

        currMax = 0

        for i in range(len(nums)):
            # if we can't reach the current element then we are stuck, return False
            # [0,1,2,3]
            # At index 0, this condition fails, and is caught in the next iteration
            # [1,2,1]
            if i > currMax:
                return False

            currMax = max(currMax, i + nums[i])
            if currMax >= len(nums):
                return True

        return True
