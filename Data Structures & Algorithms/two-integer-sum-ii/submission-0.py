class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {

        }

        for i in range(len(numbers)):
            req = target - numbers[i]

            if req in seen:
                return [seen[req], i+1]

            if numbers[i] not in seen:  
                seen[numbers[i]] = i+1
