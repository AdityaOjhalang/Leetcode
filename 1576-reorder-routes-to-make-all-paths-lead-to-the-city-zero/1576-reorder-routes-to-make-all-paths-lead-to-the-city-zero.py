class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        oldroads = set()
        graph = defaultdict(list)

        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
            oldroads.add((x,y))

        self.reorder = 0
        def dfs(node):
            for neigh in graph[node]:
                if neigh not in seen:
                    if (node,neigh) in oldroads:
                        self.reorder += 1
                    seen.add(neigh)
                    dfs(neigh)
        seen = {0}
        dfs(0)
        return self.reorder
        

