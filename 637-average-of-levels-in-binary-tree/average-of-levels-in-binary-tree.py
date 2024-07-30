# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return

        queue = deque([root])
        res = []
        while queue:
            total_nodes = len(queue)
            currsum = 0
            avg = 0
            for _ in range(total_nodes):
                node = queue.popleft()
                currsum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg = currsum / total_nodes
            res.append(avg)
        return res
