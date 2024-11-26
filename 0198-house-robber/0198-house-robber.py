class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[1],nums[0])
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(dp(i-1),dp(i-2) + nums[i])
            return memo[i]

        memo = {}
        return dp(len(nums)-1)