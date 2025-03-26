class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1,n):
            prefix.append(prefix[-1] + nums[i])
        return prefix