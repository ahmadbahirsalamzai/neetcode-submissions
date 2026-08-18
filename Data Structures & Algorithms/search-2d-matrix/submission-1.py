class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # approch: for each row check if the target element is less than the end of the row
        # if yes, then run a binary search
        # if not move to the next row

        for row in matrix:
            if row[-1] >= target:
                
                left = 0
                right = len(row)-1

                while left <= right:
                    mid = left + (right-left)//2

                    if row[mid] > target:
                        right = mid -1
                    elif row[mid] < target:
                        left = mid + 1
                    else:
                        return True


        return False