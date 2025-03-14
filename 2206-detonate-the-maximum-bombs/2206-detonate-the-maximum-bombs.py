class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i == j :
                    continue
                
                xi,yi,ri = bombs[i]
                xj,yj,rj = bombs[j]

                if ri ** 2 >= (xi-xj) ** 2 + (yi-yj) ** 2:
                    graph[i].append(j)
        
        def connected(node,seen):
            seen.add(node)
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    connected(neigh,seen)
            return len(seen)
            
        res = 0
        for i in range(n):
            seen = set()
            res = max(res,connected(i,seen))
        return res 

