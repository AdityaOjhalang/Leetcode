class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path,i,currsum):
            if currsum == target:
                res.append(path[:])
                return
            for j in range(i,len(candidates)):
                val = candidates[j]

                if val + currsum <= target:
                    path.append(val)
                    backtrack(path,j,currsum + val)
                    path.pop()
        
        backtrack([],0,0)
        return res 
