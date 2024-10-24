class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)
        
        def neighbors(ind):

            ans = []
            first = ind + arr[ind]
            second = ind - arr[ind]
            
            if 0 <= first < n:
                ans.append(first)
            if 0 <= second < n:
                ans.append(second)

            return ans 
        
        if arr[start] == 0:
            return True
            
        queue = deque([(start)])
        seen = set()
        seen.add(start)

        while queue:
            nodeinx = queue.popleft()
            if arr[nodeinx] == 0:
                return True
            
            for neigh in neighbors(nodeinx):
                if neigh not in seen:
                    seen.add(neigh)
                    queue.append(neigh)
        
        return False

        

