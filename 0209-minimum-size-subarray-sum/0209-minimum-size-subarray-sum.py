class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        size = n+1
        low = 0
        currsum = 0
        for high in range(len(nums)):
            currsum += nums[high]
            while currsum >= target:
                size = min(size,high-low+1) 
                currsum -= nums[low]
                low +=1
        if size == n+1:
            return 0
        else:    
            return size