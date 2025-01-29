class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache 
        def dp(i,cool,holding):
            if i >= len(prices):
                return 0
            
            skip = dp(i+1,False,holding)
            if not cool:
                if holding:
                    ans = max(skip, prices[i] + dp(i+1,True,False))
                else:
                    ans = max(skip, -prices[i] + dp(i+1,False,True))
            else:
                return skip

            return ans 
            
        return dp(0,False,False)
