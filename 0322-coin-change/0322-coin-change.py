class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}

        def dp(amt):
            if amt in memo:
                return memo[amt]
            mincoins = float("inf") #for cases where it is not possible
            for c in coins:
                diff = amt - c
                if diff < 0:
                    break
                mincoins = min(mincoins,dp(diff) + 1)
            memo[amt] = mincoins
            return memo[amt]
    

        res = dp(amount)
        if res < float("inf"):
            return res
        else:
            return -1
