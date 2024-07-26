# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.result = 0

        def dfs(node,currmax,currmin):
            if not node :
                return 0
            self.result = max(abs(node.val-currmax),abs(node.val-currmin) , self.result)
            currmax = max(node.val,currmax)
            currmin = min(node.val,currmin)

            dfs(node.left,currmax,currmin)
            dfs(node.right,currmax,currmin)
        
        dfs(root,root.val,root.val)

        return self.result

        