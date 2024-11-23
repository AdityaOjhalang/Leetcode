class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix) , len(matrix[0])
        left, right = 0 , (ROWS*COLS) - 1

        while left <= right:
            mid = (left+right) // 2
            row = mid // COLS
            col = mid % COLS
            midval = matrix[row][col]

            if target == midval :
                return True
            
            if target < midval:
                right = mid - 1
            if target > midval:
                left = mid + 1
        return False 

