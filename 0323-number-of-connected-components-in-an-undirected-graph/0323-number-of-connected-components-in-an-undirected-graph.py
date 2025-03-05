class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        seen = set()

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)

        components = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                components += 1
                dfs(i)

        return components 