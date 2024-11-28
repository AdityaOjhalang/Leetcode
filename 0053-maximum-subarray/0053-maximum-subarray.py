class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currmax = nums[0]
        for num in nums[1:]:
            currmax = max(num,num+currmax)
            res = max(currmax,res)
        return res