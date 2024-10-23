class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def neighbors(node):
            res = []
            for i in range(4):
                digit = str((int(node[i]) + 1) % 10)
                res.append(node[:i]+digit+node[i+1:])
                digit = str((int(node[i]) - 1) % 10)
                res.append(node[:i]+digit+node[i+1:])
            return res
        
        queue = deque([("0000",0)])
        seen = set(deadends)
        
        if "0000" in deadends:
            return -1
        
        while queue:
            node,steps = queue.popleft()

            if node == target:
                return steps

            for neigh in neighbors(node):
                if neigh not in seen:
                    seen.add(neigh)
                    queue.append((neigh,steps+1))
        
        return -1