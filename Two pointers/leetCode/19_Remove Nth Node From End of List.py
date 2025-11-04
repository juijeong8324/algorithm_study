# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Input
# the head of a linked list
# Output
# Remove the nth node from the end of the list
# Hint
# Two pointers
# Maintain two pointers and update one with a delay of n steps

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = None
        fast = head
        count = 1
        while fast.next and count < n:  # forward fast in n steps
            fast = fast.next
            count += 1

        while fast.next:  # Until End Node
            if not slow:
                slow = head
            else:
                slow = slow.next
            fast = fast.next

        if fast is slow:  # same Node
            return None

        # Remove Node
        if slow:
            target = slow.next  # nth Node
            slow.next = target.next
        else:  # If slow is None
            head = head.next

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Add Dummy Node in front of head
        # KeyPoint! This is necessary because the first node might be removed.
        slow = dummy
        fast = head

        while n > 0:
            # Question: If fast becomes None, will it cause a null error?
            # No, an error will not occur because 'n's range is guaranteed to be 1 <= n <= size.
            fast = fast.next
            n -= 1

        while fast:  # Move until fast is None
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next  # Skip slow.next Node

        return dummy.next
