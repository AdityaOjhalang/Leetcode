class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        row = set()
        col = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if i in row or j in col :
                    matrix[i][j] = 0