class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights) , len(heights[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        pac,atl = set(),set()
        
        def valid(r,c,seen,prev):
            return 0<=r<ROWS and 0<=c<COLS and (r,c) not in seen and heights[r][c] >= prev
        
        def dfs(row,col,seen,prev):
            if not valid(row,col,seen,prev):
                return 
            seen.add((row,col))
            for x,y in directions:
                nr,nc = row+x,col+y
                dfs(nr,nc,seen,heights[row][col])
        
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        res = list(pac & atl)
        return [list(cell) for cell in res]
        

