class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        
        for num in nums:
            curr = num
            streak = 0
            if (num - 1) not in numSet:
                while curr in numSet:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res