class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
       
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x,y))

        def dfs(node):
            reorder = 0
            for neigh in graph[node]:
                if neigh not in seen:
                    if (node,neigh) in roads:
                        reorder += 1
                    seen.add(neigh)
                    reorder += dfs(neigh)
            return(reorder)
        
        seen={0}
        return dfs(0)