class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphaNumaric = [char for char in s if char.isalnum()]
        first = 0
        last = len(alphaNumaric) - 1

        while first < last:
            if alphaNumaric[first] != alphaNumaric[last]:
                print(alphaNumaric[first])
                print(alphaNumaric[first])
                return False
            first += 1
            last -= 1
            
        return True