# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return None 
                
            leftail = dfs(node.left)
            rightail = dfs(node.right)

            if node.left:
                leftail.right = node.right
                node.right = node.left 
                node.left = None
            
            
            return rightail or leftail or node 
        dfs(root)