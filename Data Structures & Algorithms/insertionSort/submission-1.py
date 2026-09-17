# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return []
            
        lsts = [pairs.copy()]
        for i in range(1, len(pairs)):
            for j in range(i-1, -1, -1):
                if pairs[j].key > pairs[j+1].key:
                    tmp = pairs[j]
                    pairs[j] = pairs[j+1]
                    pairs[j+1] = tmp

            lsts.append(pairs.copy())

        return lsts 


        