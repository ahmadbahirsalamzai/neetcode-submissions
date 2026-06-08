class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = dict()
        tmap = dict()

        for i in s:
            if i in sMap:
                sMap[i] += 1
            else:
                sMap[i] = 1

        for x in t:
            if x in tmap:
                tmap[x] += 1
            else: 
                tmap[x] = 1
        
        return sMap == tmap