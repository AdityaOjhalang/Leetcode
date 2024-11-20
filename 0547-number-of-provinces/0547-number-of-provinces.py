class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        graph = defaultdict(list)
        seen = set()
        res = 0

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        def dfs(node):
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)
        
        for i in range(n):
            if i not in seen:
                seen.add(i)
                res += 1
                dfs(i)
        return res 
