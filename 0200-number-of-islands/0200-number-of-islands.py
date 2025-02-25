class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        seen = set()
        def valid(row,col):
            return 0<=row<ROWS and 0<=col<COLS
        
        def dfs(row,col):
            for x,y in directions:
                nr,nc = row+x,col+y
                if valid(nr,nc) and (nr,nc) not in seen and grid[nr][nc] == "1":
                    seen.add((nr,nc))
                    dfs(nr,nc)
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in seen and grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
                    seen.add((i,j))

        return res