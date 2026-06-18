class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r+l) // 2

            # if target is equal to mid
            if target == nums[m]:
                return m

            #left side is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    # search left side
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    # search right side
                    l = m + 1
                else:
                    r = m - 1
            
        return -1