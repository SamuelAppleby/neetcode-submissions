class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = ""
        best = ""

        for i in range(len(s)):
            found_idx = current.find(s[i])

            if found_idx != -1:
                if len(current) > len(best):
                    best = current
                
                current = current[found_idx+1:]

            current += s[i]

        if len(current) > len(best):
            best = current

        return len(best)            