class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)

        for crs,preq in prerequisites:
            graph[crs].append(preq)

        UNVISITED,VISITING,VISITED = 0,1,2
        state = [UNVISITED] * n 

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
            res.append(crs)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []

        return res 
            

            
