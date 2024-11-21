class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def valid(row,col):
            return 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] != 1
        
        ROWS = len(grid)
        COLS = len(grid[0])


        if grid[0][0] == 1:
            return -1
        
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        queue = deque([(0,0,1)])
        seen = {(0,0)}

        while queue:
            row,col,steps = queue.popleft()
            if (row,col) == (ROWS-1,COLS-1):
                return steps
            for x,y in directions:
                nr , nc = row + x , col + y
                if valid(nr,nc) and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    queue.append((nr,nc,steps+1))
        return -1

