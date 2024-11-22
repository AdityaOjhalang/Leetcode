class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def neighbors(node):
            res = []
            for i in range(len(node)):
                for char in "ACGT":
                    if node[i] != char:
                        res.append(node[:i] + char + node[i+1:])
            return res
            

        
        seen = {start}
        bank = set(bank)
        queue = deque([(start,0)])

        while queue:
            node,steps = queue.popleft()
            if node == end:
                return steps
            for neigh in neighbors(node):
                if neigh not in seen and neigh in bank:
                    seen.add(neigh)
                    queue.append((neigh,steps+1))
        return -1


