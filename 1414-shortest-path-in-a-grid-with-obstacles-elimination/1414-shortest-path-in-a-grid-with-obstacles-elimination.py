class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS #not doing element check cause we can remove obstacles
        
        ROWS , COLS = len(grid) , len(grid[0])
        seen = {(0,0,k)}
        queue = deque([(0,0,k,0)])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        while queue:
            row,col,obs,steps = queue.popleft()
            if row == ROWS - 1 and col == COLS -1:
                return steps
            for x, y in directions:
                nr , nc = row + x, col + y
                if valid(nr,nc):
                    if (nr,nc,obs) not in seen and grid[nr][nc] == 0:
                        seen.add((nr,nc,obs))
                        queue.append((nr,nc,obs,steps+1))
                    elif (nr,nc,obs-1) not in seen and grid[nr][nc] == 1 and obs:
                        seen.add((nr,nc,obs-1))
                        queue.append((nr,nc,obs-1,steps+1))
        return -1
