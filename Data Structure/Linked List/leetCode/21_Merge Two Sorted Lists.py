# Input
# the heads of two sorted liked lists list1 and list2
# Ouput
# Merge the two lists into one sorted list
# Made by splicing together

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        tail = root

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next  # move head to next Node for list1
            else:
                tail.next = list2
                list2 = list2.next  # move head to next Node for list2
            tail = tail.next  # move head to next Node for merge list

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return root.next
