"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = deque([root])

        while queue:

            num_nodes = len(queue)

            for i in range(num_nodes):
                node = queue.popleft()
                #update next pointers except the last one 
                if i < num_nodes-1:
                    node.next = queue[0]
                #add the nodes 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root




