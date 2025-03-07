"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldnew = {}
        
        def dfs(node):
            if node in oldnew:
                return oldnew[node] # copy 
            
            copy = Node(node.val)
            oldnew[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            return copy
        
        return dfs(node) if node else None


