class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sMap = {}
        l = 0
        res = 0
        wSize = 0

        for r in range(len(s)): 
            char = s[r]
            if char in sMap:
                sMap[char] += 1
            else:
                sMap[char] = 1
            
            wSize = r - l + 1
            maxV = max(sMap.values())
            if wSize - maxV > k:
                sMap[s[l]] -= 1
                l += 1
            
            res = max(res,r - l + 1)
        return res
        

            