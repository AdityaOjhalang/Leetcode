class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        ROWS,COLS = len(grid),len(grid[0])
        seen = {(0,0)}
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        queue = deque([(0,0,1)])
        n = len(grid)

        def valid(r,c):
            return 0<=r<ROWS and 0<=c<COLS and grid[r][c] == 0 and (r,c) not in seen
        
        while queue:
            row,col,steps = queue.popleft()
            if (row,col) == (ROWS-1,COLS-1):
                return steps
            for x,y in directions:
                nr,nc = row+x,col+y
                if valid(nr,nc):
                    seen.add((nr,nc))
                    queue.append((nr,nc,steps+1))
        return -1
