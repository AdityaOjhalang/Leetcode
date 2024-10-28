class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m,n = len(board),len(board[0])
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(row, col):
            if (row < 0 or row >= m or col < 0 or col >= n) or board[row][col] != "O":
                return
            board[row][col] = "E"  # Mark as visited
            for x, y in directions:
                nr, nc = row + x, col + y
                dfs(nr, nc)


        for r in range(m):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][n-1] == "O":
                dfs(r,n-1)
        
        for c in range(n):
            if board[0][c] == "O":
                dfs(0,c)
            if board[m-1][c] == "O":
                dfs(m-1,c)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "E":
                    board[i][j] = "O"        

        