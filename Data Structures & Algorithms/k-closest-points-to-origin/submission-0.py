class Solution:
    # approch:
    # first calculate all the distances for all the points and then heapify that list and then do queuepop k times
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            temp = math.sqrt(x**2 + y**2)
            heap.append([temp, x, y])

        result = []
        heapq.heapify(heap)

        for _ in range(k):
            res, x, y = heapq.heappop(heap)
            result.append([x,y])

        return result