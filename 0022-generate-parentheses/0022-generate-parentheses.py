class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path,open,close):
            if len(path) == n * 2:
                res.append("".join(path[:]))
                return 
            if open < n:
                path.append("(")
                backtrack(path,open+1,close)
                path.pop()
            if open > close:
                path.append(")")
                backtrack(path,open,close+1)
                path.pop()
        backtrack([],0,0)
        return res
            