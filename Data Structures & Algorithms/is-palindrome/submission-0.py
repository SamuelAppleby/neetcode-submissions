import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1
        s_n = ""

        for i in range(len(s)):
            if not s[i].isalnum():
                continue

            s_n += s[i].lower()
        
        for i in range(math.ceil(len(s_n)/2)):
            if s_n[i] != s_n[-1-i]:
                print(s_n[i])
                print(s_n[-1-i])
                return False

        return True