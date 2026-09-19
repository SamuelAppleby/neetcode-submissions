class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        print(nums)
        max_t = 1
        conseq = 1
        diff = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and i != len(nums) - 1:
                diff += 1
                continue

            if nums[i] - nums[i-diff] == 1:
                conseq += 1

            if i == len(nums) - 1 or nums[i] - nums[i-diff] != 1:
                if conseq > max_t:
                    max_t = conseq
                conseq = 1
                    
            diff = 1

        return max_t