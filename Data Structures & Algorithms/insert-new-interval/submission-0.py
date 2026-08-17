class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for curr in range(len(intervals)):
            # append to res
            if newInterval[1] < intervals[curr][0]:
                res.append(newInterval)
                return res + intervals[curr:]
            elif newInterval[0] > intervals[curr][1]:
                # prepend to res
                res.append(intervals[curr])
            else:
                # merge intervals
                newInterval = [
                    min(newInterval[0], intervals[curr][0]),
                    max(newInterval[1], intervals[curr][1]),
                ]
        
        res.append(newInterval)
        return res