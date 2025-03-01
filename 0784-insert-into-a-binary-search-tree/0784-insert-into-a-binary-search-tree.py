# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #main addition of node is done here
        if not root:
            return TreeNode(val)
        
        #check for possibility to be added in the left subtree
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        #check for possibility to be added in the right subtree
        if val > root.val:
            root.right = self.insertIntoBST(root.right,val)
        
        return root
