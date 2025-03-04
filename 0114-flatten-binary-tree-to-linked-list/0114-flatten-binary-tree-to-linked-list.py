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
        def dfs(root):
            if not root:
                return None
            
            leftail = dfs(root.left)
            righttail = dfs(root.right)

            if root.left:
                leftail.right = root.right
                root.right = root.left
                root.left = None 

            #non leaf nodes will have a right tail because we moved everything to rightside
            lastail = righttail or leftail or root
            return lastail 

        dfs(root)