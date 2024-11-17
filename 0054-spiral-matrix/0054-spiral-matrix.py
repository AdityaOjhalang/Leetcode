class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        top, bottom = 0, len(matrix)  # These are rows
        left, right = 0, len(matrix[0])  # These are cols

        while left < right and top < bottom :

            #going right
            for j in range(left,right):
                res.append(matrix[top][j])
            top+=1

            #going down
            for j in range(top,bottom):
                res.append(matrix[j][right-1])
            right -= 1

            if not (left < right and top < bottom ):
                break
            
            #going left 

            for j in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][j])
            bottom -=1 

            #going up
            for j in range(bottom - 1,top-1,-1):
                res.append(matrix[j][left])
            left += 1

            if not (left < right and top < bottom ):
                break
        
        return res