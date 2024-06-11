class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #calculate the transpose of the matrix
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        #reverse the colums to get the correct matrix 

        for i in range(n):
            low = 0 
            high = n-1
            while ( low < high ) :
                matrix[i][low] , matrix[i][high] = matrix[i][high],matrix[i][low]
                low+=1
                high-=1
            
        
            
        


        