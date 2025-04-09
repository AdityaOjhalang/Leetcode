# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,res):
            if not node:
                return 
            if not node.left and not node.right:
                res.append(node.val)
            
            left = dfs(node.left,res)
            right = dfs(node.right,res)
            
        res1,res2 = [],[]
        dfs(root1,res1)
        dfs(root2,res2)

        return res1 == res2