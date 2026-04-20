class Solution:

    def encode(self, strs: List[str]) -> str:
        result_str = ''
        for s in strs:
            result_str = result_str + str(len(s))+ "#" + s
        return result_str

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        
        while i < len(s):
            length_str = ''
            while i < len(s) and s[i].isdigit():
                length_str += s[i]
                i += 1
            length = int(length_str)
            temp_str = s[i+1:i + length + 1]
            result.append(temp_str)
            i += length + 1
        return result
