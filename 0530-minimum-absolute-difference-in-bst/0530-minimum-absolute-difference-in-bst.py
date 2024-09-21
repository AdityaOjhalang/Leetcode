# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sortedlist = []
        def dfs(node):
            if not node:
                return 0
            dfs(node.left)
            sortedlist.append(node.val)
            dfs(node.right)
        
        dfs(root)
        print(sortedlist)
        res = float("inf")
        for i in range(1 , len(sortedlist)):
            res = min(res, abs(sortedlist[i] - sortedlist[i-1]))
        
        return res
