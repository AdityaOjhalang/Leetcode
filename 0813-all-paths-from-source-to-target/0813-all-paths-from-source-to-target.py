class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        def backtrack(path,curr):
            if curr == target:
                res.append(path[:])
                return
            for neigh in graph[curr]:
                path.append(neigh)
                backtrack(path,neigh)
                path.pop()
        backtrack([0],0)
        return res 