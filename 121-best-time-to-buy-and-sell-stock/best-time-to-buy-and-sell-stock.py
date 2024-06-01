class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff = 0
        minval = prices[0]

        for i in range(len(prices)):
            maxdiff = max(maxdiff, prices[i] - minval)
            minval = min(minval, prices[i])
        
        return maxdiff
