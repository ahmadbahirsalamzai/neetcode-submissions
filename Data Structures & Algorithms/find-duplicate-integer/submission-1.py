class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1

        for curr in nums:
            if prev == curr:
                return curr
            prev = curr
        
        return 0