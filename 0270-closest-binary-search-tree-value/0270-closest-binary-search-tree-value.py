# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        vals = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)
        dfs(root)
        currmin = float("-inf")
        return min(vals, key = lambda x: abs(target-x))
