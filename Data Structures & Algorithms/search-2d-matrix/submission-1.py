class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        if len(matrix) == 0:
            return False
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid_row = top + (bottom - top) // 2
            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][0]:
                top = mid_row
                if mid_row + 1 < len(matrix) and target >= matrix[mid_row + 1][0]:
                    top = mid_row + 1
                else:
                    break
            else:
                return True
                

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid_col = left + (right - left) // 2 
            if target < matrix[top][mid_col]:
                right = mid_col - 1
            elif target > matrix[top][mid_col]:
                left = mid_col + 1
            else:
                return True

        return False