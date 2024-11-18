class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        hset = set(nums)
        for ind,val in enumerate(nums):
            length = 1
            if val-1 in hset:
                continue
            else:
                while val + 1 in hset:
                    val += 1
                    length +=1
            res = max(res,length)
        return res
