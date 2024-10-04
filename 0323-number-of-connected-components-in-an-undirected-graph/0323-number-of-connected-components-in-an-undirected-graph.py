class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            seen.add(node)
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)

        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()
        res = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                res += 1 
        return res
