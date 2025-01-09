class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path,i):
            if i > len(nums):
                return
            ans.append(path[:])
            for j in range(i,len(nums)):
                path.append(nums[j])
                backtrack(path,j+1)
                path.pop()
        backtrack([],0)
        return ans 