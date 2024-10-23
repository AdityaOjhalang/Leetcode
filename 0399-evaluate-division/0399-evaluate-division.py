class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(dict)

        for i in range(len(equations)):
            x,y = equations[i]
            graph[x][y] = values[i]
            graph[y][x] = 1/values[i]
        
        def querycalc(start,end):
            if start not in graph or end not in graph:
                return -1
            
            seen = {start}
            queue = deque([(start,1)])

            while queue:
                node,ratio = queue.popleft()
                if node == end:
                    return ratio
                
                for neigh in graph[node]:
                    if neigh not in seen:
                        seen.add(neigh)
                        queue.append((neigh,ratio*graph[node][neigh]))
            return -1
        
        ans = []
        for i,val in enumerate(queries):
            n,d = val
            ans.append(querycalc(n,d))
        return ans
                    

