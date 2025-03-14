class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        def neighbors(i):
            res = []
            first = i + arr[i]
            second = i - arr[i]

            if first < n:
                res.append(first)
            if second >= 0:
                res.append(second)
            return res 
            
        seen = {start}
        queue = deque([(start)])

        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True
            for neigh in neighbors(node):
                if arr[neigh] == 0:
                    return True 
                if neigh not in seen:
                    seen.add(neigh)
                    queue.append(neigh)
        return False