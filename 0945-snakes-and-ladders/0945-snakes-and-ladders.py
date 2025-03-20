class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2+1)
        label = 1
        columns = list(range(n))
        for row in range(n-1,-1,-1):
            for col in columns:
                cells[label] = (row,col)
                label += 1
            columns.reverse()

        queue = deque([(1,0)])
        seen = {1}

        while queue:
            node,steps = queue.popleft()
            if node == n**2:
                return steps
            for i in range(1,7):
                nextsq = node + i
                row,col = cells[nextsq]
                if board[row][col] != -1:
                    nextsq = board[row][col]
                if nextsq == n**2:
                    return steps + 1
                if nextsq not in seen:
                    seen.add(nextsq)
                    queue.append((nextsq,steps+1))
        return -1 
                    

