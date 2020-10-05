from collections import deque

# Definition of Node
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)
      nodes.append(node.left)
      nodes.append(node.right)
    return answer

def createBalancedBST(nums) -> Node:
    def func(nums, low, high):
        while low <= high:
            mid = low + int((high - low) / 2)
            
            root = Node(nums[mid], func(nums, low, mid - 1), func(nums, mid + 1, high))
            return root
        
        return None
        
    return func(nums, 0, len(nums) - 1)

print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7