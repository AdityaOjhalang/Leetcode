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
        queue = deque([root])
        from_right = False
        res = []
        while queue:
            total_nodes = len(queue)
            curr = []
            for _ in range(total_nodes):
                node = queue.popleft()
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if from_right:
                    res.append(reversed(curr)) #or curr[::-1]
            else:
                    res.append(curr)
            from_right = not from_right
            
        return res