class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        left, right = "l", "r"

        def dfs(node, direction, currlen):
            if not node:
                return 
            
            self.max = max(self.max, currlen)

            # Explore left child
            if node.left:
                if direction == right:
                    dfs(node.left, left, currlen + 1)  
                else:
                    dfs(node.left, left, 1)  

            # Explore right child
            if node.right:
                if direction == left:
                    dfs(node.right, right, currlen + 1)  
                else:
                    dfs(node.right, right, 1)  

        dfs(root, left, 0)
        dfs(root, right, 0)

        return self.max