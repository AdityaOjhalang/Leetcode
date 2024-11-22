class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi , yi , ri = bombs[i]
                xj , yj , rj = bombs[j]

                if ri ** 2 >= (xi - xj)**2 + (yi - yj)**2 :
                    graph[i].append(j)
        
        def connected(bomb):
            queue = deque([(bomb)])
            seen = set([i])
            while queue:
                bomb = queue.popleft()
                for neigh in graph[bomb]:
                    if neigh not in seen:
                        seen.add(neigh)
                        queue.append((neigh))
            return len(seen)
        
        ans = 0
        for i in range(n):
            ans = max(ans,connected(i))
        return ans 



