class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        for i,eq in enumerate(equations):
            a,b = eq
            graph[a].append((b,values[i]))
            graph[b].append((a,1/values[i]))
        
        def bfs(src,dst):
            if src not in graph or dst not in graph:
                return -1
            queue = deque([(src,1)])
            seen = {src}
            while queue:
                node,ratio = queue.popleft()
                if node == dst:
                    return ratio
                for neigh,weight in graph[node]:
                    if neigh not in seen:
                        seen.add(neigh)
                        queue.append((neigh,weight*ratio))
            return -1
        res = []
        for x,y in queries:
            res.append(bfs(x,y))
        return res 