# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.res = []
        def dfs(node,currsum,path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                if currsum + node.val == targetSum:
                    self.res.append(path[:])
            currsum += node.val
            left = dfs(node.left,currsum,path)
            right = dfs(node.right,currsum,path)
            path.pop()
        dfs(root,0,[])
        return self.res
            