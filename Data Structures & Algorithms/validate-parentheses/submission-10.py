class Solution:
    def isValid(self, s: str) -> bool:
        open = []

        matches = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for ch in s:
            if ch in ["(", "{", "["]:
                open.append(ch)
            else:
                if len(open) == 0 or open[-1] != matches[ch]:
                    return False
                
                open.pop()
        
        if len(open) > 0:
            return False
        
        return True