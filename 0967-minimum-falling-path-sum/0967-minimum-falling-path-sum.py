class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @cache
        def dp(row,col):

            if col <0 or col >= n:
                return float("inf")
            if row == n-1:
                return matrix[row][col]
            
            left = dp(row+1,col-1)
            middle = dp(row+1,col)
            right = dp(row+1,col+1)

            return matrix[row][col] + min(left,middle,right)
        
        return min(dp(0, col) for col in range(n))

                