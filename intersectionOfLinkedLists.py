def intersection(a, b):
    if a is None or b is None:
        return False
    
    ptr_a = a
    ptr_b = b

    while ptr_a != ptr_b:
        ptr_a = b if ptr_a is  None else  ptr_a.next
        ptr_b = a if ptr_b is None else  ptr_b.next

    return ptr_a


class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
  def prettyPrint(self):
    c = self
    while c:
      print(c.val)
      c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(7)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next
# b.next = Node(8)
b.next.next = Node(9)

c = intersection(a, b)
c.prettyPrint()
# 3 4