class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row,col):
            return 0 <= row < rows  and 0 <= col < cols and mat[row][col] == 1
        
        rows = len(mat)
        cols = len(mat[0])
        seen = set()   
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    seen.add((i,j))
                    queue.append((i,j,1))

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            row,col,steps = queue.popleft()

            for x,y in directions:
                next_r , next_c = x+row , col+y
                if valid(next_r,next_c) and (next_r,next_c) not in seen:
                    seen.add((next_r,next_c))
                    queue.append((next_r,next_c,steps+1))
                    mat[next_r][next_c] = steps
        return mat

