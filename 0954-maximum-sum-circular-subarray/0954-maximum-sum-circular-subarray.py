class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def maxsubarr(nums):
            res = nums[0]
            currmax = nums[0]
            for num in nums[1:]:
                currmax = max(currmax+num,num)
                res = max(res,currmax)
            return res
        
        total = sum(nums)
        #min subarr
        currmin = nums[0]
        minsum = nums[0]
        for num in nums[1:]:
            currmin = min(num,currmin+num)
            minsum = min(minsum,currmin)

        circularmax = total - minsum 
        normalmax = maxsubarr(nums)
        if normalmax < 0:
            return normalmax
        else:
            return max(normalmax,circularmax)