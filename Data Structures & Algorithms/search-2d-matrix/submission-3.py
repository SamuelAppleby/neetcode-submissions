class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            midpoint = int((left+right)/2)
            
            if matrix[midpoint][0] == target:
                return True

            if matrix[midpoint][0] < target:
                left = midpoint + 1

            else:
                right = midpoint - 1

        midpoint = int((left+right)/2)

        left = 0
        right = len(matrix[midpoint]) - 1
        
        while left <= right:
            midpoint1 = int((left+right)/2)

            if matrix[midpoint][midpoint1] == target:
                return True

            if matrix[midpoint][midpoint1] < target:
                left = midpoint1 + 1

            else:
                right = midpoint1 - 1

        return False



