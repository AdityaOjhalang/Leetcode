class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #vals = {value: index for index, value in enumerate(nums)}
        vals = {}
        for i in range(len(nums)):
            vals[nums[i]] = i
        n = len(nums)
        for i in range(n):
            v = target - nums[i]
            if( v in vals and vals[v] > i):
                return [i,vals[v]]               
            