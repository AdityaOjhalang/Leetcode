class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        @cache
        def dp(row,col):
            if row == col == 0:
                return 1 
            if grid[row][col] == 1:
                return 0
            ways = 0
            if row > 0:
                ways += dp(row-1,col)
            if col > 0:
                ways += dp(row,col-1)

            return ways 
        
        ROWS,COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return 0
        
        return dp(ROWS-1,COLS-1)
        