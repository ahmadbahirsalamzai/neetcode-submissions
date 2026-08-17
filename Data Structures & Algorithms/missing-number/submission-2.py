class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for curr in range(n):
            if nums[curr] != curr:
                return curr

        return n
