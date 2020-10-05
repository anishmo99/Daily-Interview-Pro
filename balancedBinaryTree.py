# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def height(root):
            if not root:
                return 0
            
            return 1 + max(height(root.left), height(root.right))
        
        lh, rh = height(root.left), height(root.right)
        
        return abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)