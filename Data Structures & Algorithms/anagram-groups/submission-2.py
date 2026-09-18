class Solution:
    def isAnagram(self, s: str, t: str):
        map_s = {}
        map_t = {}

        for c in s:
            if map_s.get(c) is None:
                map_s[c] = 1
            else:
                map_s[c] +=1

        for c in t:
            if map_s.get(c) is None:
                return False
            
            if map_t.get(c) is None:
                map_t[c] = 1
            else:
                map_t[c] +=1

                if map_t[c] > map_s[c]:
                    return False

        return map_s == map_t
            

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_s = {}

        for s in range(len(strs)):
            s_srt = ''.join(sorted(strs[s]))

            if map_s.get(s_srt) is None:
                map_s[s_srt] = [strs[s]]
            else:
                map_s[s_srt].append(strs[s])

        lsts = []
        for key, value in map_s.items():
            lsts.append(value)

        return lsts






