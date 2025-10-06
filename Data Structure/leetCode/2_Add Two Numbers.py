# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input
# two non-empty liked lists representing two positive integers
# digits are stored in reverse order
# Output
# the sum as a liked list
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            total = n1 + n2 + carry

            tail.next = ListNode(total % 10)
            carry = total // 10
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            tail.next = ListNode(carry)

        return head.next
