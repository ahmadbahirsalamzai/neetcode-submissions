class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currPath, total):
            if total == target:
                # we want to append a copy to res because we will using currPath for different combinations with currPath
                # and will end up altering the res
                res.append(currPath.copy())
                return
            # if impossible to find a combination
            if i >= len(nums) or total > target:
                return

            currPath.append(nums[i])
            dfs(i, currPath, total + nums[i])

            currPath.pop()

            dfs(i + 1, currPath, total)

        dfs(0, [], 0)

        return res