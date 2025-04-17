class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(path,currnum):
            if len(path) == n:
                res.append(currnum)
                return
            last = path[-1]
            for i in range(10):
                if abs(last - i)  == k:
                    path.append(i)
                    backtrack(path,currnum*10+i)
                    path.pop()
        res = []
        for i in range(1,10):
            backtrack([i],i)
        return res
            