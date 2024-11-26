class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            x , y = equations[i]
            val = values[i]
            graph[x].append((y,val))
            graph[y].append((x,1/val))
        
        def dfs(start,end):
            if start not in graph or end not in graph:
                return -1
            
            queue = deque([(start,1)])
            seen = {start}

            while queue:
                node,ratio = queue.popleft()
                if node == end:
                    return ratio
                
                for neigh,weight in graph[node]:
                    if neigh not in seen:
                        seen.add(neigh)
                        queue.append((neigh,weight*ratio))
            return -1
        res = []
        for x,y in queries:
            res.append(dfs(x,y))
        return res
