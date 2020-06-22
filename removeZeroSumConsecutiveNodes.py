class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0( head : Node ) -> Node:
    hashMap, runningSum = {}, 0
        cur = head 
        while cur:
            runningSum += cur.val
            if runningSum == 0:
                head = cur.next
                hashMap.clear()
            else:
                if runningSum not in hashMap:
                    hashMap[runningSum] = cur 
                else:
                    pre = hashMap[runningSum]
                    sum2 = runningSum + pre.next.val
                    while sum2 != runningSum:
                        node = hashMap[sum2]
                        del hashMap[sum2]
                        sum2 += node.next.val
                    pre.next = cur.next                    
            cur = cur.next
        return head

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
  print node.value,
  node = node.next
# 10