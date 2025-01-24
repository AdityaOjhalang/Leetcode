class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        UNVISITED,VISITING,VISITED = 0,1,2
        safe = set()
        unsafe = set()
        state = [UNVISITED] * len(graph)
        def dfs(node):
            if state[node] == VISITED:
                return True
            if state[node] == VISITING:
                return False 
            
            state[node] = VISITING
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            
            state[node] = VISITED
            return True 

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return sorted(res)

        
