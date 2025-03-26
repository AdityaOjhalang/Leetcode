class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        
        res = 0
        for i in range(n-1):
            first = prefix[i]
            last = prefix[-1] - first 
            if first >= last:
                res += 1
        return res 