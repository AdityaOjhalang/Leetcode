class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(path,i):
            if len(path) == k:
                ans.append(path[:])
                return 
            for j in range(i,n+1):
                path.append(j)
                backtrack(path,j+1)
                path.pop()
        backtrack([],1)
        return ans 