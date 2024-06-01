class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 1

        for i in range(1,len(nums)):
            if(nums[i] == nums[res]):
                count+=1
            else:
                count -= 1
            
            if(count==0):
                res=i
                count=1
        
        return nums[res]