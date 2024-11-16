class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums)-1 
        while low < high:
            currsum = nums[low]+nums[high]

            if currsum > target:
                high -= 1
            elif currsum < target:
                low+=1
            else:
                return [low+1,high+1]
        