# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        if not root:
            return None

        while queue:
            total = len(queue)
            for _ in range(total):
                curr = queue.popleft()

                curr.right , curr.left = curr.left , curr.right

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root        