class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if n==1:
            return True

        def dfs(node):
            for neigh in graph[node]:
                seen.add(node)
                if neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)

        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()
        dfs(source)

        if destination in seen:
            return True
        else:
            return False