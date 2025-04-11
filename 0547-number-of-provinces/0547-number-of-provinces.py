class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j :
                    continue
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        def dfs(node):
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)

        prov = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                prov += 1
                dfs(i)
        return prov\
