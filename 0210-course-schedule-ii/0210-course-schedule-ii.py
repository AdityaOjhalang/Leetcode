class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:

        order = []
        graph = defaultdict(list)
        for crs,preq in prerequisites:
            graph[crs].append(preq)
        
        VISITED , VISITING , UNVISITED = 2 , 1 , 0
        state = [UNVISITED] * n

        def dfs(crs):
            if state[crs] == VISITED:
                return True
            if state[crs] == VISITING:
                return False
            
            state[crs] = VISITING
            for preq in graph[crs]:
                if not dfs(preq):
                    return False
            
            state[crs] = VISITED
            order.append(crs)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        
        return order

