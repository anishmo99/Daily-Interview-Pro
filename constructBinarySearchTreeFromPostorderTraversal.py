# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def bst(root, val):
            if not root:
                return TreeNode(val)
            
            # recur
            if val < root.val:
                root.left = bst(root.left, val)
            else:
                root.right = bst(root.right, val)
            return root
        
        root = None
        for data in preorder:
            root = bst(root, data)
        
        return root