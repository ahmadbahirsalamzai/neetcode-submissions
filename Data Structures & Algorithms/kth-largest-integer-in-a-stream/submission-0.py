class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []

        for curr in self.nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, curr)
            else:
                if self.heap[0] < curr:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, curr)

    def add(self, val: int) -> int:
        # ok so we want to add a new val to an existing heap
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if self.heap[0] < val:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        
        return self.heap[0]
