# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head, l1, l2 = None, None, None

        # find head
        if list1.val <= list2.val:
            head = list1
            l1 = list1.next
            l2 = list2
        else:
            head = list2
            l2 = list2.next
            l1 = list1

        cur = head

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        
        return head
