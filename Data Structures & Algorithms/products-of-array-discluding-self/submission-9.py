class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lsts = [1] * len(nums) 
        prod = 1

        for i in range(len(nums)):
            if i != 0:
                lsts[i] = prod
            prod *= nums[i]

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums)-1:
                lsts[i] *= prod
            prod *= nums[i]

        return lsts