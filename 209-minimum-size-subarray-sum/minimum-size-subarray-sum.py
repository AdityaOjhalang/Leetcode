class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        size = n+1
        curr = 0
        for high in range(n):
            curr += nums[high]
            while(curr >= target):
                size = min(size, high-low+1)
                curr -= nums[low]
                low +=1
        if size == n+1:
            return 0
        else:    
            return size
                
                


