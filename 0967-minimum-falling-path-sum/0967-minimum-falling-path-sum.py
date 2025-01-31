class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @cache
        def dp(row,col):
            if row == n-1:
                return matrix[row][col]

            res = dp(row+1,col)
            
            if col > 0:
                res = min(dp(row+1,col-1),res)
            if col < n-1:
                res = min(dp(row+1,col+1),res)

            return matrix[row][col] + res 
        
        return min(dp(0, col) for col in range(n))

                