class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #swap the childern 
        root.left,root.right = root.right,root.left

        #invert the left and right subtree doing the same thing
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root