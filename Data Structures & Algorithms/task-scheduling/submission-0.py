# approch:
# part#1: create a map of each letter to its count
# part#3: create a max heap of the the values or count of the elements and disregard the alphbet letters..
# use a queue to keep track of what to process next.
class Solution:
    # space: O(1)
    # time: O(m) m is the number of tasks
    def leastInterval(self, tasks: List[str], n: int) -> int:
        myMap = dict()

        for i in tasks:
            myMap[i] = myMap.get(i, 0) + 1

        # create a maxHeap of values of myMap
        maxHeap = [-curr for curr in myMap.values()]
        heapq.heapify(maxHeap)

        # queue to keep track of what to process next
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
