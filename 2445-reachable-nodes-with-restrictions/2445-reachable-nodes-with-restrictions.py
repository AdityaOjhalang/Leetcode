class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        seen = {0}
        restr = set(restricted)
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        def dfs(node):
            for neigh in graph[node]:
                if neigh not in seen and neigh not in restr:
                    seen.add(neigh)
                    dfs(neigh)
        dfs(0)
        return len(seen)
