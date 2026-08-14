class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l + 1) // 2

            # if nums[mid] == target:
            #     return mid

            # if nums[mid] is greater than curr val
            if nums[mid] > target:
                r = mid - 1

            # if nums[mid] is less than curr val
            elif nums[mid] < target:
                l = mid + 1

            else: 
                return mid
        return -1
