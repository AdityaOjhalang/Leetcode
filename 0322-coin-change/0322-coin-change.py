class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0]*(amount+1)

        for amt in range(1,amount+1):
            mincoins = float("inf")
            for c in coins:
                diff = amt - c
                if diff < 0:
                    break
                mincoins = min(mincoins,dp[diff] + 1)
            dp[amt] = mincoins

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]