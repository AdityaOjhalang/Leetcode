class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        @cache
        def dp(row,col):
            if row == col == 0:
                return 1
            
            if grid[row][col] == 1:
                return 0
            
            ans = 0
            if row > 0:
                ans += dp(row-1,col)
            if col > 0:
                ans += dp(row,col-1)
            
            return ans 
        
        m ,n = len(grid),len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0
        
        return dp(m-1,n-1)
