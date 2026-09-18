ENCODE_STR = '#&^'
EMPTY = '||||'

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return EMPTY

        return ENCODE_STR.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == EMPTY:
            return []
            
        return s.split(ENCODE_STR)
