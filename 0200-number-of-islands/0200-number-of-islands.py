class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def valid(r,c):
            return 0<=r<ROWS and 0<=c<COLS and grid[r][c] == "1" and (r,c) not in seen

        def dfs(row, col):
            for x, y in directions:
                nr, nc = row + x, col + y
                if valid(nr,nc):
                    seen.add((nr,nc))
                    dfs(nr,nc)

        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if valid(i,j):
                    seen.add((i,j))
                    islands += 1
                    dfs(i,j)

        return islands
            
