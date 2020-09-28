# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            new_head = self.reverseList(head.next)
            new_tail = head.next
            new_tail.next = head
            head.next = None
            return new_head