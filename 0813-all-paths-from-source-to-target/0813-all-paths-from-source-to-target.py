class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        def backtrack(path,node):
            if node == target:
                res.append(path[:])
                return 
            for neigh in graph[node]:
                path.append(neigh)
                backtrack(path,neigh)
                path.pop()
        backtrack([0],0)
        return res