class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(path,i,currsum):
            if len(path) == k:
                if currsum == n:
                    res.append(path[:])
                return 
            
            for j in range(i,10):
                if currsum + j <= n:
                    path.append(j)
                    backtrack(path,j+1,currsum+j)
                    path.pop()
        res = []
        backtrack([],1,0)
        return res