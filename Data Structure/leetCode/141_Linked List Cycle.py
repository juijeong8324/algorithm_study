# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Input
# head = the head of a linked list
# Output
# Boolean if there is a cycle in the linked list
# Determine if the linked list has a cycle in it
# A cycle in a linked list = If there is some node in the list that can be reached again by continuously following the next pointer
# Internally pos = denote the index of the node that tail's next pointer is connected to
# Can you solve it using O(1) memory?

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = head
        node = set()
        while tail != None:
            if tail in node:  # Has Cycle
                return True

            node.add(tail)
            tail = tail.next

        return False  # If pos == -1

    # Floyd's Tortoise and Hare
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next:  # Check if the end of the list is reached
            head = head.next
            fast = fast.next.next
            if head is fast:  # Meet each other!
                return True

        return False  # Reached the end of the list, so no cycle
