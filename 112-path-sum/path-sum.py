# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, curr):
            if not node:
                return False

            # check if leaf node
            if node.left == None and node.right == None:
                return curr + node.val == targetSum

            # curr at that is shared not a common curr
            curr += node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)

            # if not leaf get true from either left or right if it exists
            return left or right

        return dfs(root, 0)
