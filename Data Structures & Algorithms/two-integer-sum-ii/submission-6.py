class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev_req = None
        for i in range(len(numbers)):
            if numbers[i] < 0 and target < 0:
                req = abs(numbers[i])- abs(target)
            else:
                req = target - numbers[i]

            if req == prev_req:
                continue

            prev_req = req

            for j in range(i+1, len(numbers)):
                if numbers[j] == req:
                    return [i+ 1, j+1]

                if numbers[j] > req:
                    break
