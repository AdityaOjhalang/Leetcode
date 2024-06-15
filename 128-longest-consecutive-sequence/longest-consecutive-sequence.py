class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hset = set(nums)
        res = 0

        for num in hset:
            if num - 1 not in hset:
                length = 1
                curr = num

                while curr+1 in hset:
                    length+=1
                    curr +=1

                res = max(res,length)
        
        return res