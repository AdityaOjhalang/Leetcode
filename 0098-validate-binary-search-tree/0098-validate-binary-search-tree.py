# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower = float("-inf"), upper = float("inf")):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            left = dfs(node.left,lower,val)
            right = dfs(node.right,val,upper)

            return left and right
        
        return dfs(root)
        