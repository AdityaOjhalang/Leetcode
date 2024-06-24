class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #vals = {value: index for index, value in enumerate(nums)}
        vals = {}
        res = []
        for i , n in enumerate(nums):
            
            if (target - n) not in vals:
                vals[n] = i
            
            else :
                return [vals[target-n] , i]

        return []