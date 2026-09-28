class Solution:
    def search(self, nums: List[int], target: int, left: int = -1, right: int = -1) -> int:
        if left == -1:
            left = 0
            right = len(nums) -1

        midpoint = int((left + right) / 2)
        print(f'left: {left}')
        print(f'mid: {midpoint}')
        print(f'right: {right}')

        if left == right and nums[midpoint] != target:
            return -1

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            if nums[midpoint+1] > target:
                return -1

            return self.search(nums, target, midpoint+1, right)
        else:
            if nums[midpoint-1] < target:
                return -1

            return self.search(nums, target, left, midpoint)

