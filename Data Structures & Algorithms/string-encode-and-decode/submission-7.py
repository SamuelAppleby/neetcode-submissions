class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''

        for s in strs:
            ret += f'{len(s)}#{s}'

        return ret

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []

        while i < len(s) - 1:
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1

            i += 1
            print(length)
            length = int(length)
            word = s[i:i+length]
            strs.append(word)

            i+= length

        return strs
