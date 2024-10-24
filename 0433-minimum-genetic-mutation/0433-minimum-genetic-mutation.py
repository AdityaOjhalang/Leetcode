class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        def mutations(node):
            arr = []

            for i in range(len(node)):
                if node[i] == "A":
                    arr.append(node[:i] + "C" + node[i+1:])
                    arr.append(node[:i] + "G" + node[i+1:])
                    arr.append(node[:i] + "T" + node[i+1:])
                if node[i] == "C":
                    arr.append(node[:i] + "A" + node[i+1:])
                    arr.append(node[:i] + "G" + node[i+1:])
                    arr.append(node[:i] + "T" + node[i+1:])
                if node[i] == "G":
                    arr.append(node[:i] + "A" + node[i+1:])
                    arr.append(node[:i] + "C" + node[i+1:])
                    arr.append(node[:i] + "T" + node[i+1:])
                if node[i] == "T":
                    arr.append(node[:i] + "A" + node[i+1:])
                    arr.append(node[:i] + "C" + node[i+1:])
                    arr.append(node[:i] + "G" + node[i+1:])
                    
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