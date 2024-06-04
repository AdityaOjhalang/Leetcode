class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low = 0
        high = n-1

        while low < high:
            sum = nums[low] + nums[high]
            if(sum > target):
                high-=1
            elif(sum < target):
                low+=1
            else:
                return [low+1,high+1]


        
