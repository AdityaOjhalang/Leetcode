class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            if node.left is None:
                return 1 + dfs(node.right)
            elif node.right is None:
                return 1 + dfs(node.left)
            return 1 + min(dfs(node.left),dfs(node.right))
        return dfs(root)