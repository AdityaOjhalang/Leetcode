class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #helper function to check whether the position is valid and is an island or not 
        def valid(row, col):
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1"
        #recrusive DFS to find all neighbors in the set
        def dfsNeigh(row, col):
            for x, y in directions:
                nextrow, nextcol = row + x, col + y
                if valid(nextrow,nextcol) and (nextrow,nextcol) not in seen:
                    seen.add((nextrow,nextcol))
                    dfsNeigh(nextrow,nextcol)
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        #going in all directions to find neighbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        #running the funciton
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in seen:
                    seen.add((i,j))
                    res +=1
                    dfsNeigh(i,j)
        return res