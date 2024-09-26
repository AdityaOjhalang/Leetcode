# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.res = 0

        def dfs(node,currnum):
            if not node:
                return
            
            # check if we have reached the leaf node:
            if not node.left and not node.right:
                self.res += currnum*10 + node.val
                return
            
            currnum = currnum*10 + node.val
            dfs(node.left,currnum)
            dfs(node.right,currnum)
        
        dfs(root,0)
        return self.res