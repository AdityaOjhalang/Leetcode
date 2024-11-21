class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def neighbors(node):
            res = []
            for i in range(4):
                digit = str((int(node[i]) + 1) % 10 )
                res.append(node[:i] + digit + node[i+1:])
                digit = str((int(node[i]) - 1) % 10 )
                res.append(node[:i] + digit + node[i+1:])
            return res


        seen = set(deadends)
        if "0000" in deadends:
            return -1
        
        queue = deque([("0000",0)])
        seen.add("0000")

        while queue:
            node,turns = queue.popleft()
            if node == target:
                return turns
            for neigh in neighbors(node):
                if neigh not in seen:
                    seen.add(neigh)
                    queue.append((neigh,turns+1))
        return - 1