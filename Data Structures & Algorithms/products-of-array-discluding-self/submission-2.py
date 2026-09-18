class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1

        zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero != -1:
                    prod = 0 
                    break
                else:
                    zero = i
            else:
                prod *= nums[i]

        for i in range(len(nums)):
            if zero == i:
                res.append(int(prod))
            elif zero == -1:
                res.append(int(prod / nums[i]))
            else:
                res.append(0)
                
        return res