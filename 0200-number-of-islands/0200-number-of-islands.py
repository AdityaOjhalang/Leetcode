class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()

        def valid(row,col):
            return 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == "1"

        def dfs(row,col):
            for x,y in directions:
                nr , nc = row + x , col + y
                if valid(nr,nc) and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    dfs(nr,nc)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in seen:
                    seen.add((i,j))
                    res += 1
                    dfs(i,j)
        return res 



