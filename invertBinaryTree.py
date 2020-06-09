class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
  
    def preorder(self):
        print self.value,
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()

def invert(root):
    if root is None:
        return
    
    invert(root.left)
    invert(root.right)
    
    temp=root.left
    root.left=root.right
    root.right=temp
    

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')

root.preorder()
# a b d e c f
print "\n"
invert(root)
root.preorder()
# a c f b e d
