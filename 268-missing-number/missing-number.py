class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        hset = set(nums)
        n = len(nums)
        if n not in hset:
            return n
        for i in range (n):
            if i not in hset:
                return i
            
