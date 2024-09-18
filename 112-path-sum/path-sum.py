# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node,curr):
            if not node:
                return False
            #check when we reach a leaf node if it is equal to target 
            if not node.left  and  not node.right:
                return (curr + node.val  == targetSum)
            
            curr += node.val
            left = dfs(node.left,curr)
            right = dfs(node.right,curr)
            # we are good with answer from either left or right 
            return left or right

        return dfs(root,0)