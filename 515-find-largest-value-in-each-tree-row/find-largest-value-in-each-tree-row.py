# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue  = deque([root])
        res = []
        while queue:
            level_len = len(queue)
            currmax = float('-inf')
            for _ in range(level_len):
                node = queue.popleft()
                if node.val > currmax:
                    currmax = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(currmax)
        return res



        