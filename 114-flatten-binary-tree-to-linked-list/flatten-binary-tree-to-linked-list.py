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
        arr = []
        def dfs(node):
            if not node:
                return
            arr.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        # Reconstruct the tree to form the linked list
        print(len(arr))
        for i in range(len(arr) - 1):
            arr[i].left = None
            arr[i].right = arr[i + 1]

        if arr:
            arr[-1].left = None
            arr[-1].right = None

