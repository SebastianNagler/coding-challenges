# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev_list = None
        while head:
            rev_list = ListNode(val=head.val, next=rev_list)
            head = head.next

        return rev_list