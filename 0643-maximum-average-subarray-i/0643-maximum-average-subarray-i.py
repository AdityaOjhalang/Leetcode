class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = currsum = 0
        for i in range(k):
            currsum += nums[i]
        ans = currsum / k
        for i in range(k,len(nums)):
            currsum += nums[i] - nums[i-k]
            ans = max(ans,currsum/k)
        return ans 
