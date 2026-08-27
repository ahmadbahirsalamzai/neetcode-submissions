class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # time = O(n logm)
        # space = O(1)

        maxPile = max(piles)
        left, right = 1, maxPile
        res = 0

        while left <= right:
            k = left + (right - left) // 2

            # calculate the new hours using the new k aka k
            hours = sum(math.ceil(x / k) for x in piles)

            # update left or right based on the new hours needed to finish in given time
            if hours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res
