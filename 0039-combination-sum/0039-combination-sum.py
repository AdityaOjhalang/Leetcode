class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path,i,currsum):
            if currsum == target:
                res.append(path[:])
                return 
            for j in range(i,len(candidates)):
                if currsum + candidates[j] <= target:
                    path.append(candidates[j])
                    backtrack(path,j,currsum+candidates[j])
                    path.pop()
        res = []
        backtrack([],0,0)
        return res 