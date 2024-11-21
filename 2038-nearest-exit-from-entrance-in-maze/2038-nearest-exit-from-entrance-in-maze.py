class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and maze[r][c] == "."
        def validExit(r,c):
            return (r in {0,ROWS-1} or c in {0,COLS-1}) and (r,c) != (x,y) and maze[r][c] == "."
        
        ROWS , COLS = len(maze) , len(maze[0])
        x,y = entrance
        queue = deque([(x,y,0)])
        seen = {(x,y)}
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while queue:
            row, col, steps = queue.popleft()
            if validExit(row,col):
                return steps
            for x,y in directions:
                nr,nc = row+x,col+y
                if valid(nr,nc) and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    queue.append((nr,nc,steps+1))
        return -1


        

