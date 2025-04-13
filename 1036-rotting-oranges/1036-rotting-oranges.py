class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        fresh = 0
        FRESH,ROTTEN = 1,2
        queue = deque()

        def valid(r,c):
            return 0<=r<m and 0<=c<n and grid[r][c] == FRESH
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    queue.append((i,j))
                if grid[i][j] == FRESH:
                    fresh += 1
        time = -1
        if fresh == 0:
            return 0

        while queue:
            tot = len(queue)
            time += 1
            for _ in range(tot):
                row,col = queue.popleft()
                for x,y in directions:
                    nr,nc = row+x,col+y
                    if valid(nr,nc):
                        grid[nr][nc] = ROTTEN 
                        fresh -= 1
                        queue.append((nr,nc))
        if fresh == 0:
            return time
        else:
            return -1