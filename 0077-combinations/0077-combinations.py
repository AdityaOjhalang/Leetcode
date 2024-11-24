class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(curr,i):
            if len(curr) == k:
                ans.append(curr[:])
                return 
            
            for j in range(i,n+1):
                curr.append(j)
                backtrack(curr,j+1)
                curr.pop()
        
        backtrack([],1)
        return ans

            