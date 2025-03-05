class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if n == 1:
            return True
        
        graph = defaultdict(list)
        seen = {source}

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            if node == destination:
                return
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)
        
        dfs(source)
        if destination in seen:
            return True
        else:
            return False
            