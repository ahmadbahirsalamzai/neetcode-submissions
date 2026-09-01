class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = float("-inf")

        for curr in nums:
            if prev == curr:
                return curr
            prev = curr
        
        return 0