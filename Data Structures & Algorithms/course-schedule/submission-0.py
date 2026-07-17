class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build a map course -> preReq
        courseMap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            courseMap[c].append(p)

        visiting = set()

        def dfs(curr):
            if curr in visiting:
                return False
            if not courseMap[curr]:
                return True

            # add the course to the vistin set
            visiting.add(curr)
            # if the current item has prerequisites then call dfs on each one
            for i in courseMap[curr]:
                if not dfs(i):
                    return False

            # rest the visiting and make the list of preReqs empty for the course and return true
            courseMap[curr] = []
            visiting.remove(curr)
            return True

        for temp in range(numCourses):
            if not dfs(temp):
                return False

        return True
