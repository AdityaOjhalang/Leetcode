class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        def valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0

        n = len(grid)
        seen = {(0, 0)}
        queue = deque([(0, 0, 1)])
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
        ]
        while queue:
            row,col,steps = queue.popleft()
            
            if (row,col) == (n-1,n-1):
                return steps
            
            for x,y in directions:
                next_r,next_c = row+x , col+y
                if valid(next_r,next_c) and (next_r,next_c) not in seen:
                    seen.add((next_r,next_c))
                    queue.append((next_r,next_c,steps+1))
        
        return -1
                