class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(r,c):
            return 0<=r<m and 0<=c<n and maze[r][c] == "." and (r,c) not in seen
        def validExit(r,c):
            return ( r in {0,m-1} or  c in {0,n-1}) and (r,c) != (x_start,x_end) 
        
        m,n = len(maze) , len(maze[0])
        x_start , x_end = entrance
        queue = deque([(x_start,x_end,0)])
        seen = {(x_start,x_end)}
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            row, col, steps = queue.popleft()
            if validExit(row,col):
                return steps
            for x,y in directions:
                nr,nc = row+x,col+y
                if valid(nr,nc):
                    if validExit(nr,nc):
                        return steps+1
                    seen.add((nr,nc))
                    queue.append((nr,nc,steps+1))
        return -1