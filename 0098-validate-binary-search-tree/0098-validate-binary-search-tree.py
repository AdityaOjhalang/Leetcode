# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node,low = float("-inf"), high = float("inf")):
            if not node:
                return True
            if node.val <= low or node.val >= high :
                return False
            left = check(node.left,low,node.val)
            right = check(node.right,node.val,high)

            return left and right
        return check(root)