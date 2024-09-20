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
        res = []
        right = False
        queue = deque([root])
        while queue:
            num_nodes = len(queue)
            curr_level = []
            for _ in range(num_nodes):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if right:
                res.append(reversed(curr_level))
            else:
                res.append(curr_level)
                
            right = not right
            
        return res