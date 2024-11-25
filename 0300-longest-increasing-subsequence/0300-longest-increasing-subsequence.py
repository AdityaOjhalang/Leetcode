class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dp(i):
            if i in memo:
                return memo[i]
            ans = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans,dp(j)+1)
            memo[i] = ans
            return memo[i]
        memo = {}
        return max(dp(i) for i in range(len(nums)))

            
