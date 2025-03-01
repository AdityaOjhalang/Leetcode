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

        self.maxvalue = float("-inf")

        def dfs(node, currmax, currmin):
            if not node:
                return 0
            self.maxvalue = max(
                self.maxvalue, abs(currmax - node.val), abs(currmin - node.val)
            )
            currmax = max(currmax,node.val)
            currmin = min(currmin,node.val)

            left = dfs(node.left,currmax,currmin)
            right = dfs(node.right,currmax,currmin)

        dfs(root,root.val,root.val)
        return self.maxvalue 
