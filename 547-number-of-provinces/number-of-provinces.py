class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                ans+=1
                seen.add(i)
                dfs(i)
        return ans