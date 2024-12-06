class Solution:
    def uniquePaths(self, ROWS: int, COLS: int) -> int:
        dp = [[1]*COLS for _ in range(ROWS)] #basecase

        for i in range(1,ROWS):
            for j in range(1,COLS):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[ROWS-1][COLS-1]