class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        for s in strs:
            sorted_el = ''.join(sorted(s))
            if sorted_el in map:
                map[sorted_el].append(s)
            else:
                map[sorted_el] = [s]
        return list(map.values())