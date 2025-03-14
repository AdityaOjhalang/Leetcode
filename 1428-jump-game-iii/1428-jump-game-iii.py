class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def neighbors(ind):
            res = []
            first = ind + arr[ind]
            second = ind - arr[ind]

            if first < len(arr):
                res.append(first)
            if second >= 0:
                res.append(second)
            return res
        
        if arr[start] == 0:
            return True
        
        queue = deque([(start)])
        seen = {start}

        while queue:
            ind = queue.popleft()
            if arr[ind] == 0:
                return True
            for neigh in neighbors(ind):
                if neigh not in seen:
                    seen.add(neigh)
                    queue.append(neigh)
        return False