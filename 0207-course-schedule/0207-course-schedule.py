class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for crs,preq in prerequisites:
            graph[crs].append(preq)
        
        state = [0] * n
        UNVISITED,VISITING,VISITED = 0,1,2

        def dfs(crs):
            if state[crs] == VISITING:
                return False
            if state[crs] == VISITED:
                return True
            
            state[crs] = VISITING
            for preq in graph[crs]:
                if not dfs(preq):
                    return False
            
            state[crs] = VISITED 
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        return True 
