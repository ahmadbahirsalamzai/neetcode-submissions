class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)

        for i in range(n+1):
            temp = i
            while temp:
                res[i] += 1 if temp & 1 == 1 else 0
                temp >>= 1

        return res
