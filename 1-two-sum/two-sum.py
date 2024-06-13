class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        vals = {value: index for index, value in enumerate(nums)}
        n = len(nums)
        for i in range(n):
            v = target - nums[i]
            if( v in vals and vals[v] > i):
                return [i,vals[v]]               
            