class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(log(n*m))
        # Space: O(1)
        cols = len(matrix[0])
        rows = len(matrix)

        left = 0
        right = (cols * rows) - 1

        while left <= right:
            mid = left + (right - left) // 2

            row = mid // cols
            col = mid % cols

            currMid = matrix[row][col]
    
            if currMid > target:
                right = mid - 1
            elif currMid < target:
                left = mid + 1
            else:
                return True

        return False