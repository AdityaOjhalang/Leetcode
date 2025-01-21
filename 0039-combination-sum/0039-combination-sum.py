class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path,i,currsum):
            if currsum == target:
                res.append(path[:])
                return
            for j in range(i,len(candidates)):
                num = candidates[j]
                if num + currsum <= target:
                    path.append(num)
                    backtrack(path,j,currsum+num)
                    path.pop()
        
        res = []
        backtrack([],0,0)
        return res