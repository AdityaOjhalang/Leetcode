class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        hset = set(nums)
        for val in (nums):
            if val-1 not in hset:
                length = 1
                while val + 1 in hset:
                    val += 1
                    length +=1
                res = max(res,length)
        return res
