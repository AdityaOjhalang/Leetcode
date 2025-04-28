class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array where dp[i] means minimum coins needed for amount i
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0
        
        # Build the dp array from 1 to amount
        for i in range(1, amount + 1):
            for coin in coins:
                # Only try to use the coin if it doesn't exceed the current amount
                if i - coin >= 0:
                    # Update dp[i] if using this coin gives a better answer
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        # If dp[amount] is still the initial large value, return -1 (not possible)
        return dp[amount] if dp[amount] != amount + 1 else -1