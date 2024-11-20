# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node,low=float("-inf"),high=float("inf")):
            if not node:
                return True
            val = node.val
            if val <= low or val >= high:
                return False
            
            left = check(node.left,low,val)
            right = check(node.right,val,high)

            return left and right
        return check(root)