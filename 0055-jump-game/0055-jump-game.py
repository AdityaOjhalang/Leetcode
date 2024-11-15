class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        n = len(nums) 
        for i in range(n-2,-1,-1):
            if ( nums[i] + i ) >= goal:
                goal = i
        
        return goal == 0