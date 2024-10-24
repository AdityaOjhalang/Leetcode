class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if (ri**2) >= ((xi - xj) ** 2 + (yi - yj) ** 2):
                    graph[i].append(j)
        
        def bfs(i):
            queue = deque([i])
            seen = set([i])
            while queue:
                bomb = queue.popleft()
                for neigh in graph[bomb]:
                    if neigh not in seen:
                        seen.add(neigh)
                        queue.append(neigh)
            return len(seen)

        ans = 0

        for i in range(n):
            ans = max(ans,bfs(i))
        
        return ans
        

