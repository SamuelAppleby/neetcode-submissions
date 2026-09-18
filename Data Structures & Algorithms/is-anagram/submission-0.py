class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for c in s:
            if map_s.get(c) is None:
                map_s[c] = 1
            else:
                map_s[c] += 1

        for c in t:
            if map_s.get(c) is None:
                return False
            
            if map_t.get(c) is None:
                map_t[c] = 1
            else:
                map_t[c] += 1

                if map_t[c] > map_s[c]:
                    return False

        return map_s == map_t