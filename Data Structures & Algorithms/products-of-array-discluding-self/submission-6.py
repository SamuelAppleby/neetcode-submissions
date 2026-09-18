class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_up_to = [1] * len(nums)
        prod = 1

        for i in range(len(nums)):
            prod *= nums[i]
            prod_up_to[i] = prod

        prod_from = [1] * len(nums)
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            prod_from[i] = prod

        lsts = []
        for i in range(len(nums)):
            if i == 0:
                lsts.append(prod_from[i+1])
            elif i == len(nums) - 1:
                lsts.append(prod_up_to[i-1])
            else:
                lsts.append(prod_up_to[i-1] * prod_from[i+1])

        return lsts