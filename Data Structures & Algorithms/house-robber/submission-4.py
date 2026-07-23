class Solution:
    # time = O(n)
    # Space = O(1)
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return

        prev1 = 0
        prev2 = 0

        # itterate through the list of nums
        for i in range(len(nums)):
            temp = prev1
            prev1 = prev2 + nums[i] if prev2 + nums[i] > prev1 else prev1

            prev2 = temp

        return prev1
