# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        l = 1
        cur = head
        
        while cur.next:
            cur = cur.next
            l += 1
            
        k = l - k % l
        cur.next = head
        
        while k:
            cur = cur.next
            k -= 1
            
        head = cur.next
        cur.next = None
        
        return head