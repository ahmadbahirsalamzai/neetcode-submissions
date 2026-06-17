class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s == t: 
            return s

        # createa a mapping of char -> count
        myMap = Counter(t)

        currMap = dict()
        # add elements of window that are in t only
        currCount = 0

        l = 0

        res = [-1,-1]
        resLen = float("infinity")


        count = 0

        for r in range(len(s)):
            char = s[r]
            if char in myMap:
                currMap[char] = 1 + currMap.get(char, 0)
            else:
                currMap[char] = 1

            if char in myMap and currMap[char] == myMap[char]:
                count += 1
            
            while count == len(myMap):
                if r - l + 1 < resLen:
                    res = [l,r]
                    resLen = r - l + 1
            
                currMap[s[l]] -= 1
                
                if s[l] in myMap and currMap[s[l]] < myMap[s[l]]:
                    count -= 1
                
                l += 1
        l,r = res

        if resLen == float("infinity"):
            return ""

        return s[l:r+1]