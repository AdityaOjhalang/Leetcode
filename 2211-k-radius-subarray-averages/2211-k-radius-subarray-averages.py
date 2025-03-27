class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1,n):
            prefix.append(prefix[-1] + nums[i])
        res = [-1]*n
        for i in range(len(nums)):
            if i < k or i + k >= n :
                continue
            if i - k == 0:
                res[i] = prefix[i+k] // (2*k+1)
            else:
                res[i] = (prefix[i+k] - prefix[i-k-1]) // ((2 * k + 1))
        return res 
            