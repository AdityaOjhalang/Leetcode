class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 1
        
        while queue:
            num_nodes = len(queue)

            for _ in range(num_nodes):
                node = queue.popleft()

                if node.left == None and node.right == None:
                    return depth
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1
        return -1