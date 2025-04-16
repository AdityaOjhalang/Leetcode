class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path,i):
            if i > len(nums):
                return 
            
            res.append(path[:])
            for j in range(i,len(nums)):
                path.append(nums[j])
                backtrack(path,j+1)
                path.pop()
        res = []
        backtrack([],0)
        return res 