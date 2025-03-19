class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for crs,preq in prerequisites:
            graph[crs].append(preq)
        
        UNVISITED, VISITING, VISITED = 0,1,2
        states = [UNVISITED] * n

        def dfs(crs):
            if states[crs] == VISITING:
                return False
            if states[crs] == VISITED:
                return True
            
            states[crs] = VISITING

            for preq in graph[crs]:
                if not dfs(preq):
                    return False
            
            states[crs] = VISITED
            return True 
        
        for i in range(n):
            if not dfs(i):
                return False 
        return True 