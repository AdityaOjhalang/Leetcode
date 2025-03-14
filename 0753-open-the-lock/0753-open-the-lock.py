class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        seen = set(deadends)
        seen.add("0000")

        def dfs(node):
            res = []
            for i in range(4):
                num = int(node[i])
                for change in [-1,1]:
                    x = (change + num) % 10
                    res.append(node[0:i] + str(x) + node[i+1:])
            return res
        
        queue = deque([("0000",0)])
        while queue:
            num,steps = queue.popleft()
            if num == target:
                return steps
            for neigh in dfs(num):
                if neigh not in seen:
                    seen.add(neigh)
                    queue.append((neigh,steps+1))
        return -1

