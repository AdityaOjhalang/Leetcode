class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        size = n + 1
        start = 0
        cursum = 0
        for end in range(n):
            cursum += nums[end]
            while cursum >= target:
                size = min(size,end-start+1)
                cursum -= nums[start]
                start += 1
        return 0 if size == n + 1 else size
