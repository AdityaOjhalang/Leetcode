class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(n))
        for i in range(n-1,-1,-1):
            for j in columns:
                cells[label] = (i,j)
                label += 1
            columns.reverse
        
        visited = {1}
        queue = deque([(1,0)])

        while queue:
            square,rolls = queue.popleft()
            if cells[square] == n*n:
                return rolls 
            for i in range(7):
                nextsq = square + i
                row,col = cells[nextsq]
                if board[row][col] != -1:
                    nextsq = board[row][col]
                if nextsq == n * n:
                    return rolls + 1
                if nextsq not in visited:
                    visited.add(nextsq)
                    queue.append((nextsq,rolls+1))
        return -1 


