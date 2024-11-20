# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        right = False
        queue = deque([root])
        res = []
        while queue:
            num = len(queue)
            level = []
            for _ in range(num):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if right:
                res.append(list(reversed(level)))
            else:
                res.append(level)
            right = not right
        return res