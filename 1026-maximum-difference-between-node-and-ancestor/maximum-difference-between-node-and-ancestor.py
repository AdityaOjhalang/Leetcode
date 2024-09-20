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

        self.maxvalue = float('-inf')
        def dfs(node,currmin,currmax):
            if not node:
                return 0 
            self.maxvalue = max(self.maxvalue , abs(currmax - node.val) , abs(node.val - currmin))
            currmax = max(currmax,node.val)
            currmin = min(currmin,node.val)

            # Don't need to return anything as we are only concerned with the maxvalue
            left = dfs(node.left,currmin,currmax)
            right = dfs(node.right,currmin,currmax)

        dfs(root,root.val,root.val)
        return self.maxvalue

