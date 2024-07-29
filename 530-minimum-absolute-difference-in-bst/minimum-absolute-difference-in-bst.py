# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.sortednodes = []
        def dfs(node):
            if not node:
                return 0
            dfs(node.left)
            self.sortednodes.append(node.val)
            dfs(node.right)
            
        dfs(root)
        res = float('inf')
        for i in range(1,len(self.sortednodes)):
            res = min(res,self.sortednodes[i] -  self.sortednodes[i-1])
        return res



        