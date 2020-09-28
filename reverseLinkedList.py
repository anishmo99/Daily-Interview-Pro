# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        next = None
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        head = prev
        return head