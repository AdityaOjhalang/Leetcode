# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,currmax):
            if not node:
                return 0

            count  = 0
            if node.val >= currmax:
                count = 1
                currmax = node.val
            
            count += dfs(node.left,currmax)
            count += dfs(node.right,currmax)

            return count

        return dfs(root,root.val)