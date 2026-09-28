class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # Step 1: Count number of nodes
        cur = head
        count = 0

        while cur:
            count += 1
            cur = cur.next

        # If removing the first node
        if n == count:
            return head.next

        # Step 2: Find the node BEFORE the one we want to remove
        prev = head

        # Target node from front is:
        # count - n + 1
        #
        # So prev should stop at:
        # count - n
        for _ in range(count - n - 1):
            prev = prev.next

        # Step 3: Skip the node
        prev.next = prev.next.next

        return head