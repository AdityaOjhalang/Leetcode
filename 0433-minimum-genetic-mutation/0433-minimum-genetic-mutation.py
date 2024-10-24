class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        def mutations(node):
            arr = []

            for i in range(len(node)):
                for char in "ACGT":
                    if char != node[i]:
                        arr.append(node[:i] + char + node[i+1:])    
            return arr
        
        queue = deque([(startGene,0)])
        seen = {startGene}
        bank = set(bank)

        while queue:
            node,steps = queue.popleft()

            if node == endGene:
                return steps 

            for neigh in mutations(node):
                if neigh not in seen:
                    seen.add(neigh)

                    if neigh in bank:
                        queue.append((neigh,steps+1))
        return -1 