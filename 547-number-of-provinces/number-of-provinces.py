class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #check all neighbors of the node and if it is there add to the set
        def dfs(node):
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)
        #build the graph of is connected (of all the neighbors)
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        #create the set
        seen = set()
        ans = 0
        #build our answer 
        for i in range(n):
            if i not in seen: #if node not in set add it 
                ans += 1
                seen.add(i)
                dfs(i) #and check all neighbors and add them as well

        return ans
