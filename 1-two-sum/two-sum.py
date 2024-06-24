class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #vals = {value: index for index, value in enumerate(nums)}
        vals = {}
        res = []
        for i , n in enumerate(nums):
            complement = target - n
            if complement in vals:
                return [vals[complement],i]
            vals[n] = i
        return []