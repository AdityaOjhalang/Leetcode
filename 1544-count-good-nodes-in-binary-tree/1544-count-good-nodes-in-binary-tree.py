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
            
            count = 0
            if node.val >= currmax:
                currmax = node.val
                count = 1
            
            leftcount = dfs(node.left ,currmax)
            rightcount = dfs(node.right,currmax)

            return leftcount + rightcount + count 
        
        return dfs(root,root.val)