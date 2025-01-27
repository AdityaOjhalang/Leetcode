class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}

        def dp(amt):
            if amt in memo:
                return memo[amt]
            mincoins = float("inf")
            for c in coins:
                diff = amt - c
                if diff < 0:
                    break
                mincoins = min(mincoins,dp(diff) + 1)
            memo[amt] = mincoins 
            return mincoins
        
        result = dp(amount)
        if result < float("inf"):
            return result 
        else:
            return -1 