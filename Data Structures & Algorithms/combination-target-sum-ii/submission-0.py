class Solution:
    # check all the subsets and add the ones that add up to teh target. 
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        currSum = 0
        currList = []

        def dfs(i, currSum):
            if currSum == target:
                res.append(currList[:])
                return
            if i >= len(candidates) or currSum > target:
                return

            curr = candidates[i]

            currList.append(curr)
            dfs(i+1, currSum + curr)

            currList.pop()

            while i < len(candidates) and candidates[i] == curr:
                i += 1

            dfs(i, currSum)
        
        dfs(0, 0)
        return res


        