class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS,COLS = len(board),len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def valid(r,c):
            return 0<=r<ROWS and 0<=c<COLS and board[r][c] == "O"


        def edgedfs(row,col):
            if not valid(row,col):
                return 
            board[row][col] = "E"
            for x,y in directions:
                nr,nc = row+x,col+y
                if valid(nr,nc):
                    edgedfs(nr,nc)

        for col in range(COLS):
            if board[0][col] == "O":
                edgedfs(0,col)
            if board[ROWS-1][col] == "O":
                edgedfs(ROWS-1,col)
        for row in range(ROWS):
            if board[row][0] == "O":
                edgedfs(row,0)
            if board[row][COLS-1] == "O":
                edgedfs(row,COLS-1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "E":
                    board[i][j] = "O"
                

