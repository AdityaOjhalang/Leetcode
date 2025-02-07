class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        @cache
        def dp(i,j):
            if i >= m or j >= n:
                return 0
            
            if matrix[i][j] == '0':
                return 0
            
            right = dp(i,j+1)
            down = dp(i+1,j)
            diag = dp(i+1,j+1)

            return 1 + min(right,down,diag)
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res , dp(i,j))
    
        return res  ** 2