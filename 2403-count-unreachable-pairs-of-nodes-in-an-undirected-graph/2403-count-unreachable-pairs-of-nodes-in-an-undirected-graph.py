class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Recursive DFS to find the size of a connected component
        def dfs(node):
            visited.add(node)
            size = 1  # Current node counts as 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    size += dfs(neighbor)
            return size
        
        # Find all connected components
        visited = set()
        component_sizes = []
        for i in range(n):
            if i not in visited:
                component_sizes.append(dfs(i))
        
        # Calculate unreachable pairs
        total_pairs = n * (n - 1) // 2
        reachable_pairs = sum(size * (size - 1) // 2 for size in component_sizes)
        return total_pairs - reachable_pairs
