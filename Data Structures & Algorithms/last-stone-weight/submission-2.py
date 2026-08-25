class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # time: O(nlong(n)), because for each element in the stones list we have to do push and pop operations which are O(log(ng)) worst case
        # space: O(n)
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, (first - second))

        stones.append(0)
        return abs(stones[0])
