class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(row,col):
            return 0<=row<rows and 0<=col<cols and grid[row][col] == 1

        def dfs(row,col):
            seen.add((row, col))
            area = 1
            for x,y in directions:
                next_r , next_c = row+x , col+y
                if valid(next_r,next_c) and (next_r,next_c) not in seen:
                    seen.add((next_r,next_c))
                    area += dfs(next_r,next_c)
            return area
        
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1),(-1,0),(1,0),(0,-1)] 
        res = 0

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in seen and grid[i][j] == 1:
                    res = max(res,dfs(i,j))
        return res
                    
                    

