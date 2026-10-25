class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])

        res = []
        res.append(intervals[0][:])

        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            prevEnd = res[-1][1]

            if start <= prevEnd:
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start,end])
        
        return res

