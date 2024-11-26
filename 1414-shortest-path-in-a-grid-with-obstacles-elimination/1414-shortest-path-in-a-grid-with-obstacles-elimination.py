class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        m,n = len(grid) , len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = deque([(0,0,k,0)])
        seen = {(0,0,k)}

        def valid(r,c):
            return 0<=r<m and 0<=c<n

        while queue:
            row,col,rem,steps = queue.popleft()
            if row == m-1 and col == n-1:
                return steps
            for x,y in directions:
                nr,nc = row+x,col+y
                if valid(nr,nc):
                    if (nr,nc,rem) not in seen and grid[nr][nc] == 0:
                        seen.add((nr,nc,rem))
                        queue.append((nr,nc,rem,steps+1))
                    elif (nr,nc,rem-1) not in seen and grid[nr][nc] == 1 and rem:
                        seen.add((nr,nc,rem-1))                                
                        queue.append((nr,nc,rem-1,steps+1))
        return -1