# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        rev1, rev2 = self.reverseList(list1), self.reverseList(list2)
        while rev1 or rev2:
            if (not rev2) or (rev1 and rev1.val > rev2.val):
                rev1_copy = rev1
                rev1 = rev1.next
                rev1_copy.next = rev
                rev = rev1_copy
            else:
                rev2_copy = rev2
                rev2 = rev2.next
                rev2_copy.next = rev
                rev = rev2_copy
        
        return rev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head:
            next = head.next
            head.next = rev
            rev = head
            head = next

        return rev