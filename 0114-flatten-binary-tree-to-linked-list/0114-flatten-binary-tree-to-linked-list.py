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
        res = []
        def dfs(node):
            if not node:
                return 
            res.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        for i in range(len(res)):
            if i + 1 < len(res) :
                res[i].left = None 
                res[i].right = res[i+1]
        
        if res:
            res[-1].left = None
            res[-1].right = None
        
        return res