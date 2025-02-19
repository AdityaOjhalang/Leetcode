class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        leftsum = 0
        for i, num in enumerate(nums):
            if leftsum == (totalsum - num - leftsum):
                return i
            leftsum += num
        return -1