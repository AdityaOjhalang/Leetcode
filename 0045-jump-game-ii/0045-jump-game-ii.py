class Solution:
    def jump(self, nums: List[int]) -> int:
        minjumps = 0
        farthest = 0
        currend = 0
        for i in range(len(nums)-1):
            farthest = max(farthest,nums[i]+i)

            if i == currend:
                currend = farthest
                minjumps += 1
            
            if currend >= len(nums) - 1:
                break
        return minjumps