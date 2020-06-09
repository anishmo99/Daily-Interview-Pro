# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, A, B, c = 0):
    
    if A is None:
        return B
        
    if B is None:
        return A
    
    carry,sum=0,0
    sum=A.val+B.val+carry
    A=A.next
    B=B.next
    newHead=ListNode(sum%10)
    newHeadPtr=newHead
    carry=sum/10
    
    
    while(A is not None or B is not None or carry):
        sum=(A.val if A is not None else 0)+(B.val if B is not None else 0)+carry
        temp=ListNode(sum%10)
        carry=sum/10
        newHead.next=temp
        newHead=newHead.next
        if A is not None:
            A = A.next
        if B is not None:
            B = B.next
    
    
    return newHeadPtr


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8
