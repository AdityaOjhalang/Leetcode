class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(i,j):
            if i == j == 0:
                return grid[i][j]
            
            ans = float("inf")
            if i > 0:
                ans = min(ans,dp(i-1,j))
            if j > 0:
                ans = min(ans,dp(i,j-1))
            
            return ans + grid[i][j]
            
        m = len(grid)
        n = len(grid[0])
        return dp(m-1,n-1)