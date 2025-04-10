# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        res = float("-inf")
        lvl = 1
        maxlvl = 0
        while queue:
            tot = len(queue)
            currsum = 0
            for _ in range(tot):
                node = queue.popleft()
                currsum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if currsum > res:
                res = currsum
                maxlvl = lvl
            lvl += 1
        return maxlvl
