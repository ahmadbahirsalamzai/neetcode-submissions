class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solve this problem with bucket sort. 
        map = dict()
        result = [[] for _ in range(len(nums) + 1)]

        # count each num add add to a map
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        # bucket sort the elementsin the map
        for num,freq in map.items():
            result[freq].append(num)
        
        #iterate through the result array and add the k last elements to a final result and return
        finalResult = []
        count = 0
        for i in reversed(result):
            for el in i:
                if len(finalResult) == k:
                    return finalResult
                finalResult.append(el)
                count +=1
        return finalResult