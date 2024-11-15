class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff = float('-inf')
        minval = prices[0]

        for i in range(1,len(prices)):
            maxdiff = max(maxdiff,prices[i]-minval)
            minval = min(prices[i],minval)

        return max(maxdiff,0)