class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_n = {}

        for num in nums:
            if map_n.get(num) is None:
                map_n[num] = 1
            else:
                map_n[num] += 1

        map_n = {k:v for k, v in sorted(map_n.items(), key=lambda item: -item[1])}

        freq = []
        for i in range(k):
            freq.append(list(map_n.keys())[i])

        return freq