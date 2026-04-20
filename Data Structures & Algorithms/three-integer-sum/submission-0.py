class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j + 1, n):
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue
                    numSum = int(nums[i]) + int(nums[j]) + int(nums[k])
                    if numSum == 0:
                        el = [nums[i], nums[j], nums[k]]
                        res.append(el)
        return res