from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.res = 0  # Use this as shared state

        hmap = defaultdict(int)
        hmap[0] = 1  # Needed to handle exact matches from root

        def dfs(node, currsum, hmap):
            if not node:
                return
            currsum += node.val
            compl = currsum - targetSum
            self.res += hmap.get(compl, 0)
            hmap[currsum] += 1

            dfs(node.left, currsum, hmap)
            dfs(node.right, currsum, hmap)

            hmap[currsum] -= 1  # Backtrack

        dfs(root, 0, hmap)
        return self.res  # ← This line MUST be self.res