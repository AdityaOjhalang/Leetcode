class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            for neigh in rooms[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)
        seen = {0}
        dfs(0)
        return len(rooms) == len(seen)