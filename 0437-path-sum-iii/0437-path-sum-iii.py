from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.res = 0  

        hmap = defaultdict(int)
        hmap[0] = 1 

        def dfs(node, currsum, hmap):
            if not node:
                return
            currsum += node.val
            compl = currsum - targetSum
            self.res += hmap.get(compl, 0)
            hmap[currsum] += 1

            dfs(node.left, currsum, hmap.copy())
            dfs(node.right, currsum, hmap.copy())

        dfs(root, 0, hmap)
        return self.res  