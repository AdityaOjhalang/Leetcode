class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n 

        def backtrack(row, col, i, seen):
            if i == len(word):
                return True

            for x, y in directions:
                nr, nc = row + x, col + y
                if valid(nr, nc) and (nr, nc) not in seen and board[nr][nc] == word[i]:
                    seen.add((nr, nc))
                    if backtrack(nr, nc, i + 1, seen):
                        return True
                    seen.remove((nr, nc))
            return False

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(row, col, 1, {(row, col)}):
                    return True
        return False
