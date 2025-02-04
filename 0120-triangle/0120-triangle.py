class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(row,col):
            if row == n-1:
                return triangle[row][col]
            
            left = dp(row+1,col)
            right = dp(row+1,col+1)

            res = min(left,right)
            return triangle[row][col] + res

        n = len(triangle)
        return dp(0,0)