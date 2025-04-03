class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n

        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i]
        
        suffix[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i]
        
        for i in range(n):
            if i == 0:
                res[i] = suffix[i+1]
            elif i == n-1:
                res[i] = prefix[i-1]
            else:
                res[i] = suffix[i+1] * prefix[i-1] 

        return res 