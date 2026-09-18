class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        fracs = [1] * len(nums)
        zero = -1

        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
                fracs[i] = 1/nums[i]
            else:
                if zero != -1:
                    res = [0] * len(nums)
                    return res
                zero = i
                fracs[i] = 1

        res = [prod] * len(nums)

        for i in range(len(nums)):
            if zero == i or zero == -1:
                res[i] = int(res[i] * fracs[i])
            elif zero != -1:
                res[i] = 0

        return res