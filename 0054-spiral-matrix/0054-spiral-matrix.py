class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        top, bot = 0, len(matrix)
        l, r = 0, len(matrix[0])

        while l < r and top < bot:

            #going right
            for j in range(l,r):
                res.append(matrix[top][j])
            top += 1
            
            #going down
            for i in range(top,bot):
                res.append(matrix[i][r-1])
            r -= 1

            if not (l < r and top < bot):
                break 

            #going left
            for j in range(r-1,l-1,-1):
                res.append(matrix[bot-1][j])
            bot -= 1

            #going top
            for i in range(bot-1,top-1,-1):
                res.append(matrix[i][l])
            l += 1

            if not (l < r and top < bot):
                break 
            
        return res
