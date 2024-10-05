class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        def dfs(node):
            seen.add(node)
            for neigh in graph[node]:
                if neigh not in seen and neigh not in restr:
                    seen.add(neigh)
                    dfs(neigh)

        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        restr = set(restricted)
        seen = set()
        dfs(0)
        return len(seen)