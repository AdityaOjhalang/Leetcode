class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def neighbors(node):
            res = []
            for i in range(len(node)):
                for char in "ACGT":
                    if char != node:
                        res.append(node[0:i] + char + node[i+1:])
            return res
        
        queue = deque([(startGene,0)])
        bank = set(bank)
        seen = {startGene}

        while queue:
            node,steps = queue.popleft()
            if node == endGene:
                return steps
            for neigh in neighbors(node):
                if neigh not in seen and neigh in bank:
                    seen.add(neigh)
                    queue.append((neigh,steps+1))
        
        return -1
