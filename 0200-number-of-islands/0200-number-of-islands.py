class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(row, col):
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1"

        def dfsNeigh(row, col):
            for x, y in directions:
                nextrow, nextcol = row + x, col + y
                if valid(nextrow,nextcol) and (nextrow,nextcol) not in seen:
                    seen.add((nextrow,nextcol))
                    dfsNeigh(nextrow,nextcol)
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in seen:
                    seen.add((i,j))
                    res +=1
                    dfsNeigh(i,j)
        return res