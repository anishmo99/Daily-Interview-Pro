class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None



# maxLevel : keeps track of maximum  
# level seen so far.  
# res : Value of deepest node so far.  
# level : Level of root  
def find(root, level, maxLevel, res): 
  
    if (root != None): 
        level += 1
        find(root.left, level, maxLevel, res)  
  
        # Update level and resue  
        if (level > maxLevel[0]): 
          
            res[0] = root.data  
            maxLevel[0] = level  
          
        find(root.right, level, maxLevel, res)  
          
# Returns value of deepest node  
def deepestNode(root) : 
  
    # Initialze result and max level  
    res = [-1]  
    maxLevel = [-1]  
  
    # Updates value "res" and "maxLevel"  
    # Note that res and maxLen are passed  
    # by reference.  
    find(root, 0, maxLevel, res)  
    return (res[0],maxLevel[0])



root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepestNode(root))
# (d, 3)