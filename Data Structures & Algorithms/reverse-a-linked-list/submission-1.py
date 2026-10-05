# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = None
        l = temp
        c = head
        r = c.next

        while c:
            c.next = l
            if r:
                l = c
                c = r
                r = r.next
            else:
                return c