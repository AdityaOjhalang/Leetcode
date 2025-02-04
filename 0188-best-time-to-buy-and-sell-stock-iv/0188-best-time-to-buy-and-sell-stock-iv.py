class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(i, holdings, remain):
            if i >= len(prices) or remain == 0:
                return 0

            skip = dp(i + 1, holdings, remain)

            if holdings: #we can either sell or skip take max of both
                ans = max(skip, prices[i] + dp(i + 1, False, remain - 1))
            else: #we can either buy or skip take max of both
                ans = max(skip, -prices[i] + dp(i + 1, True, remain))
                
            return ans 

        return dp(0,False,k)