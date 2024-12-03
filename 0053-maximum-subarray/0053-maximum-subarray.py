class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = currmax = nums[0]
        for num in nums[1:]:
            currmax = max(num , currmax+num)
            res = max(res,currmax)
        return res 