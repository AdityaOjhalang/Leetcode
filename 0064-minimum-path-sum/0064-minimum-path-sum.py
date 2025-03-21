class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            if row == col == 0:
                return grid[0][0]

            ans = float("inf")
            if row > 0:
                ans = min(ans, dp(row - 1, col))
            if col > 0:
                ans = min(ans, dp(row, col - 1))
            
            return ans + grid[row][col]
        
        m = len(grid)
        n = len(grid[0])

        return dp(m-1,n-1)
        

