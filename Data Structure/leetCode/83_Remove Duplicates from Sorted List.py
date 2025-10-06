# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input
# head = the head of a sorted liked list
# Output
# delete all duplicates such that each element appears only once
class Solution:
    # With Dummy Node
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(101, None)
        tail = root
        while head != None:
            if tail.val != head.val:
                tail.next = head
                tail = tail.next  # update

            head = head.next

        tail.next = None
        return root.next

    # In-place
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next  # skip curr.next
            else:
                curr = curr.next  # forward
        return head
